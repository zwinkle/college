document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.getElementById('new-task');
    const addTaskBtn = document.getElementById('add-task-btn');
    const taskListIncomplete = document.getElementById('task-list-incomplete');
    const taskListComplete = document.getElementById('task-list-complete');

    function saveTasks() {
        const tasks = [];
        document.querySelectorAll('li').forEach(item => {
            tasks.push({
                text: item.querySelector('.task-text').textContent.trim(),
                completed: item.classList.contains('completed')
            });
        });
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    function loadTasks() {
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks.forEach(task => {
            addTaskToList(task.text, task.completed, false);
        });
    }

    function addTaskToList(taskText, completed = false, withAnimation = true) {
        const listItem = document.createElement('li');

        const taskTextElement = document.createElement('span');
        taskTextElement.textContent = taskText;
        taskTextElement.classList.add('task-text');

        const completeBtn = document.createElement('button');
        completeBtn.textContent = completed ? 'Undo' : 'Selesai';
        completeBtn.classList.add('complete-btn');
        completeBtn.addEventListener('click', function() {
            listItem.classList.toggle('completed');
            completeBtn.textContent = listItem.classList.contains('completed') ? 'Undo' : 'Selesai';
            moveTask(listItem);
            saveTasks();
        });

        const editBtn = document.createElement('button');
        editBtn.textContent = 'Edit';
        editBtn.classList.add('edit-btn');
        editBtn.addEventListener('click', function() {
            const currentText = taskTextElement.textContent.trim();
            const editInput = document.createElement('input');
            editInput.type = 'text';
            editInput.value = currentText;
            taskTextElement.replaceWith(editInput);
            editInput.focus();

            const saveEdit = () => {
                const newText = editInput.value.trim();
                if (newText !== '') {
                    editInput.replaceWith(taskTextElement);
                    taskTextElement.textContent = newText;
                    saveTasks();
                }
            };

            editInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    saveEdit();
                }
            });

            editInput.addEventListener('blur', saveEdit);
        });

        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'Hapus';
        removeBtn.classList.add('remove-btn');
        removeBtn.addEventListener('click', function() {
            const confirmDelete = confirm('Apakah Anda yakin ingin menghapus tugas ini?');
            if (confirmDelete) {
                listItem.remove();
                saveTasks();
            }
        });

        listItem.appendChild(taskTextElement);
        listItem.appendChild(completeBtn);
        listItem.appendChild(editBtn);
        listItem.appendChild(removeBtn);

        if (completed) {
            listItem.classList.add('completed');
        }

        if (withAnimation) {
            listItem.classList.add('adding');
            setTimeout(() => listItem.classList.remove('adding'), 500);
        }

        moveTask(listItem);

        saveTasks();
    }

    function addTask() {
        const taskText = taskInput.value.trim();
        if (taskText === '') {
            alert('Tugas tidak boleh kosong!');
            return;
        }
        addTaskToList(taskText);
        taskInput.value = '';
    }

    function moveTask(listItem) {
        if (listItem.classList.contains('completed')) {
            taskListComplete.appendChild(listItem);
        } else {
            taskListIncomplete.appendChild(listItem);
        }
    }

    addTaskBtn.addEventListener('click', addTask);

    taskInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            addTask();
        }
    });

    loadTasks();
});
