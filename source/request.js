//Проверка на наличие токена
function HaveToken() {
    return new Promise(function(resolve, reject) {
        let token = localStorage.getItem('api_token');
        if (token) {
            MainFunc();
        } else {
            getToken();
        }
    })
}

// Запрашиваем токен

function getToken(){
    return $.ajax({
        data : JSON.stringify({username: 'admin', password : 'admin'}),
        method: 'post',
        url : 'http://localhost:8000/api/v1/login/',
        contentType:'application/json',
        dataType : 'json',
        success:function(response, status) {console.log(response); localStorage.setItem('api_token', response.token);},
        error: function(response, status) {console.log(response);}
    });
}


// Выбор всех задач
function getIssues(){
    $.ajax({
        method: 'get',
        url : 'http://localhost:8000/api/v1/issues/',
        headers : {'Authorization' : 'Token ' + localStorage.getItem('api_token') },
        dataType : 'json',
        success:function(response, status) {console.log(response);},
        error: function(response, status) {console.log(response);}
    });
}


// Выбор всех проектов
function getProjects(){
    $.ajax({
        method: 'get',
        url : 'http://localhost:8000/api/v1/projects/',
        headers : {'Authorization' : 'Token ' + localStorage.getItem('api_token') },
        dataType : 'json',
        success:function(response, status) {console.log(response);},
        error: function(response, status) {console.log(response);}
    });
}


//Выбор всех задач заданного проекта
function getSomeIssues(){
    $.ajax({
        method: 'get',
        url : 'http://localhost:8000/api/v1/issues/?project=1',
        headers : {'Authorization' : 'Token ' + localStorage.getItem('api_token') },
        dataType : 'json',
        success:function(response, status) {console.log(response);},
        error: function(response, status) {console.log(response);}
    });
}

// Создание задачи;
function createIssue(){
    $.ajax({
        data : JSON.stringify({
            assigned_to: 16,
            created_by: 17,
            description: "Тест",
            project: 5,
            status: 2,
            tip: 1,
            title: "Тест2"
        }),
        method: 'post',
        headers : {'Authorization' : 'Token ' + localStorage.getItem('api_token') },
        url : 'http://localhost:8000/api/v1/issues/',
        contentType:'application/json',
        dataType : 'json',
        success:function(response, status) {console.log(response + 'Данные успешно добавлены!');},
        error: function(response, status) {console.log(response);}
    });
}


// Удаление задачи.
function delIssue(){
    $.ajax({
        method: 'delete',
        url : 'http://localhost:8000/api/v1/issues/28',
        headers : {'Authorization' : 'Token ' + localStorage.getItem('api_token') },
        dataType : 'json',
        success:function(response, status) {console.log(response + 'Успешно удалено!') ;},
        error: function(response, status) {console.log(response);}
    });
}

function MainFunc()
{
    getIssues();
    getProjects();
    getSomeIssues();
    createIssue();
    delIssue();
}

HaveToken();
