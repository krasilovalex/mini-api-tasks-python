```markdown
### **Запуск тестов**
```bash
pip install -r requirements.txt
pytest test_api.py -v
```

### **Запуск через Docker**
```bash
docker build -t mini-api-tasks .
docker run -d -p 8000:8000 --name my-task-api mini-api-tasks
```

**SwaggerUI**: [http://localhost:8000/docs](http://localhost:8000/docs)

### **Endpoints**
* `POST /tasks` — создать новую задачу.
* `GET /tasks` — получить список всех задач.
* `GET /tasks/{id}` — получить задачу по ID.

### **Тесты**
```text
test_api.py::test_create_task PASSED                                                [ 16%]
test_api.py::test_get_tasks_empty PASSED                                            [ 33%]
test_api.py::test_get_tasks_with_data PASSED                                        [ 50%]
test_api.py::test_get_task_by_id_success PASSED                                     [ 66%]
test_api.py::test_get_task_by_id_not_found PASSED                                   [ 83%]
test_api.py::test_create_task_validation_error PASSED                               [100%]
```
```
