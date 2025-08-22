// Global variables
let students = [];
let filteredStudents = [];
let currentEditingId = null;

// DOM elements
const studentsTableBody = document.getElementById('studentsTableBody');
const studentModal = document.getElementById('studentModal');
const deleteModal = document.getElementById('deleteModal');
const studentForm = document.getElementById('studentForm');
const loading = document.getElementById('loading');
const noData = document.getElementById('noData');
const searchInput = document.getElementById('searchInput');
const statusFilter = document.getElementById('statusFilter');
const toast = document.getElementById('toast');

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    loadStudents();
    loadStats();
});

// Event Listeners
function setupEventListeners() {
    // Modal controls
    document.getElementById('addStudentBtn').addEventListener('click', openAddModal);
    document.getElementById('closeModal').addEventListener('click', closeModal);
    document.getElementById('cancelBtn').addEventListener('click', closeModal);
    document.getElementById('closeDeleteModal').addEventListener('click', closeDeleteModal);
    document.getElementById('cancelDeleteBtn').addEventListener('click', closeDeleteModal);
    
    // Form submission
    studentForm.addEventListener('submit', handleFormSubmit);
    
    // Delete confirmation
    document.getElementById('confirmDeleteBtn').addEventListener('click', handleDelete);
    
    // Search and filter
    searchInput.addEventListener('input', filterStudents);
    statusFilter.addEventListener('change', filterStudents);
    
    // Close modal on outside click
    window.addEventListener('click', function(event) {
        if (event.target === studentModal) {
            closeModal();
        }
        if (event.target === deleteModal) {
            closeDeleteModal();
        }
    });
    
    // Set today's date as default enrollment date
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('enrollmentDate').value = today;
}

// API Functions
async function loadStudents() {
    try {
        showLoading(true);
        const response = await fetch('/api/students');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        students = await response.json();
        filteredStudents = [...students];
        renderStudents();
        showLoading(false);
    } catch (error) {
        console.error('Error loading students:', error);
        showToast('Error loading students. Please try again.', 'error');
        showLoading(false);
        showNoData(true);
    }
}

async function loadStats() {
    try {
        const response = await fetch('/api/stats');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const stats = await response.json();
        updateHeaderStats(stats);
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

async function saveStudent(studentData) {
    try {
        const url = currentEditingId ? `/api/students/${currentEditingId}` : '/api/students';
        const method = currentEditingId ? 'PUT' : 'POST';
        
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(studentData),
        });
        
        const result = await response.json();
        
        if (!response.ok) {
            throw new Error(result.error || 'Failed to save student');
        }
        
        return result;
    } catch (error) {
        throw error;
    }
}

async function deleteStudent(studentId) {
    try {
        const response = await fetch(`/api/students/${studentId}`, {
            method: 'DELETE',
        });
        
        const result = await response.json();
        
        if (!response.ok) {
            throw new Error(result.error || 'Failed to delete student');
        }
        
        return result;
    } catch (error) {
        throw error;
    }
}

// UI Functions
function renderStudents() {
    if (filteredStudents.length === 0) {
        showNoData(true);
        return;
    }
    
    showNoData(false);
    
    studentsTableBody.innerHTML = filteredStudents.map(student => `
        <tr>
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.email}</td>
            <td>${student.phone || 'N/A'}</td>
            <td>${student.course}</td>
            <td>${getOrdinalNumber(student.semester)}</td>
            <td>${formatDate(student.enrollment_date)}</td>
            <td>
                <span class="status-badge status-${student.status.toLowerCase()}">
                    ${student.status}
                </span>
            </td>
            <td class="actions">
                <button class="btn-icon btn-edit" onclick="openEditModal(${student.id})" title="Edit">
                    <i class="fas fa-edit"></i>
                </button>
                <button class="btn-icon btn-delete" onclick="openDeleteModal(${student.id})" title="Delete">
                    <i class="fas fa-trash"></i>
                </button>
            </td>
        </tr>
    `).join('');
}

function updateHeaderStats(stats) {
    document.getElementById('totalStudents').textContent = stats.total_students;
    document.getElementById('activeStudents').textContent = stats.active_students;
}

function filterStudents() {
    const searchTerm = searchInput.value.toLowerCase();
    const statusValue = statusFilter.value;
    
    filteredStudents = students.filter(student => {
        const matchesSearch = !searchTerm || 
            student.name.toLowerCase().includes(searchTerm) ||
            student.email.toLowerCase().includes(searchTerm) ||
            student.course.toLowerCase().includes(searchTerm);
        
        const matchesStatus = !statusValue || student.status === statusValue;
        
        return matchesSearch && matchesStatus;
    });
    
    renderStudents();
}

// Modal Functions
function openAddModal() {
    currentEditingId = null;
    document.getElementById('modalTitle').textContent = 'Add New Student';
    document.getElementById('submitBtnText').textContent = 'Add Student';
    studentForm.reset();
    
    // Set default values
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('enrollmentDate').value = today;
    document.getElementById('studentStatus').value = 'Active';
    
    studentModal.style.display = 'block';
    document.body.classList.add('modal-open');
    document.getElementById('studentName').focus();
}

function openEditModal(studentId) {
    const student = students.find(s => s.id === studentId);
    if (!student) return;
    
    currentEditingId = studentId;
    document.getElementById('modalTitle').textContent = 'Edit Student';
    document.getElementById('submitBtnText').textContent = 'Update Student';
    
    // Populate form
    document.getElementById('studentName').value = student.name;
    document.getElementById('studentEmail').value = student.email;
    document.getElementById('studentPhone').value = student.phone || '';
    document.getElementById('studentCourse').value = student.course;
    document.getElementById('studentSemester').value = student.semester;
    document.getElementById('enrollmentDate').value = student.enrollment_date;
    document.getElementById('studentStatus').value = student.status;
    
    studentModal.style.display = 'block';
    document.body.classList.add('modal-open');
    document.getElementById('studentName').focus();
}

function closeModal() {
    studentModal.style.display = 'none';
    document.body.classList.remove('modal-open');
    studentForm.reset();
    currentEditingId = null;
}

function openDeleteModal(studentId) {
    const student = students.find(s => s.id === studentId);
    if (!student) return;
    
    document.getElementById('deleteStudentInfo').innerHTML = 
        `<strong>${student.name}</strong> (${student.email})`;
    
    deleteModal.style.display = 'block';
    document.body.classList.add('modal-open');
    
    // Store student ID for deletion
    document.getElementById('confirmDeleteBtn').setAttribute('data-student-id', studentId);
}

function closeDeleteModal() {
    deleteModal.style.display = 'none';
    document.body.classList.remove('modal-open');
}

// Form Handlers
async function handleFormSubmit(event) {
    event.preventDefault();
    
    const submitBtn = document.getElementById('submitBtn');
    const submitBtnText = document.getElementById('submitBtnText');
    const btnLoading = document.getElementById('btnLoading');
    
    // Show loading state
    submitBtnText.style.display = 'none';
    btnLoading.style.display = 'flex';
    submitBtn.disabled = true;
    
    try {
        const formData = new FormData(studentForm);
        const studentData = {
            name: formData.get('name'),
            email: formData.get('email'),
            phone: formData.get('phone'),
            course: formData.get('course'),
            semester: parseInt(formData.get('semester')),
            enrollment_date: formData.get('enrollment_date'),
            status: formData.get('status')
        };
        
        await saveStudent(studentData);
        
        closeModal();
        loadStudents();
        loadStats();
        
        const action = currentEditingId ? 'updated' : 'added';
        showToast(`Student ${action} successfully!`, 'success');
        
    } catch (error) {
        console.error('Error saving student:', error);
        showToast(error.message || 'Error saving student. Please try again.', 'error');
    } finally {
        // Reset button state
        submitBtnText.style.display = 'inline';
        btnLoading.style.display = 'none';
        submitBtn.disabled = false;
    }
}

async function handleDelete() {
    const studentId = document.getElementById('confirmDeleteBtn').getAttribute('data-student-id');
    if (!studentId) return;
    
    try {
        await deleteStudent(studentId);
        closeDeleteModal();
        loadStudents();
        loadStats();
        showToast('Student deleted successfully!', 'success');
    } catch (error) {
        console.error('Error deleting student:', error);
        showToast(error.message || 'Error deleting student. Please try again.', 'error');
    }
}

// Utility Functions
function showLoading(show) {
    loading.style.display = show ? 'flex' : 'none';
    document.getElementById('studentsTable').style.display = show ? 'none' : 'table';
}

function showNoData(show) {
    noData.style.display = show ? 'block' : 'none';
    document.getElementById('studentsTable').style.display = show ? 'none' : 'table';
}

function showToast(message, type = 'info') {
    const toastContent = toast.querySelector('.toast-content');
    const toastIcon = toast.querySelector('.toast-icon');
    const toastMessage = toast.querySelector('.toast-message');
    
    // Set icon based on type
    let iconClass = 'fas fa-info-circle';
    if (type === 'success') iconClass = 'fas fa-check-circle';
    else if (type === 'error') iconClass = 'fas fa-exclamation-circle';
    else if (type === 'warning') iconClass = 'fas fa-exclamation-triangle';
    
    toastIcon.className = `toast-icon ${iconClass}`;
    toastMessage.textContent = message;
    toast.className = `toast toast-${type} show`;
    
    // Auto hide after 3 seconds
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

function formatDate(dateString) {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

function getOrdinalNumber(num) {
    const suffixes = ['th', 'st', 'nd', 'rd'];
    const value = num % 100;
    return num + (suffixes[(value - 20) % 10] || suffixes[value] || suffixes[0]);
}