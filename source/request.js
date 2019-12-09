// Запрашиваем токен
$.ajax({
data : JSON.stringify({username: 'admin', password : 'admin'}),
method: 'post',
url : 'http://localhost:8000/api/v1/login/',
contentType:'application/json',
dataType : 'json',
success:function(response, status) {console.log(response); localStorage.setItem('api_token', response.token);},
error: function(response, status) {console.log(response);}
});

// Выбор всех задач

$.ajax({
method: 'get',
url : 'http://localhost:8000/api/v1/issues/',
headers : {'Authorization' : 'Token ' + localStorage.getItem('api_token') },
dataType : 'json',
success:function(response, status) {console.log(response);},
error: function(response, status) {console.log(response);}
});

// Выбор всех проектов

$.ajax({
method: 'get',
url : 'http://localhost:8000/api/v1/projects/',
headers : {'Authorization' : 'Token ' + localStorage.getItem('api_token') },
dataType : 'json',
success:function(response, status) {console.log(response);},
error: function(response, status) {console.log(response);}
});

//Выбор всех задач заданного проекта

// Создание задачи;

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



// Удаление задачи.

$.ajax({
method: 'delete',
url : 'http://localhost:8000/api/v1/issues/28',
headers : {'Authorization' : 'Token ' + localStorage.getItem('api_token') },
dataType : 'json',
success:function(response, status) {console.log(response + 'Успешно удалено!') ;},
error: function(response, status) {console.log(response);}
});


