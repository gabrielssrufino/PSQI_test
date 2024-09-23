function mostrarErro(mensagem) {
    Swal.fire({
        toast: true,
        position: "top-end",
        icon: "error",
        title: "Erro!",
        text: mensagem,
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true
    });
}

function createChart(response) {
    var ctx = document.getElementById('myChart').getContext('2d');

    const formattedLabels = response.labels.map(label => {
        const date = new Date(label);
        return date.toLocaleDateString('pt-BR', { day: 'numeric', month: 'numeric', year: 'numeric' });
    });

    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: formattedLabels,
            datasets: [{
                label: 'Pontuação PSQI',
                data: response.data,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                fill: false
            }]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'Qualidade do Sono ao Longo do Tempo',
                    font: {
                        size: 18
                    }
                },
                subtitle: {
                    display: true,
                    text: 'Pontuação PSQI (0-5: Boa, 5-10: Pobre, 10+: Distúrbio)',
                    font: {
                        size: 12,
                        style: 'italic',
                        color: '#BB86FC'
                    },
                    padding: {
                        bottom: 20
                    }
                }
            },
            tooltips: {
                callbacks: {
                    label: function(tooltipItem) {
                        return response.quality_map[tooltipItem.index];
                    },
                    title: function() {
                        return '';
                    }
                }
            }
        }
    });
}

function createResult(data) {
    document.querySelector('#backToMenu1').classList.remove('transparent')
    let list = document.querySelector('.history ul');
    list.innerHTML = '';
    
    data.labels.forEach(function(label, index) {
        let date = new Date(label);
        let formattedDate = date.toLocaleDateString();
        let quality = data.quality_map[index];

        let listItem = document.createElement('li');
        let dateParagraph = document.createElement('p');
        let qualityParagraph = document.createElement('p');

        dateParagraph.textContent = formattedDate;
        qualityParagraph.textContent = quality;

        listItem.appendChild(dateParagraph);
        listItem.appendChild(qualityParagraph);

        list.appendChild(listItem);
    });
}

let userEmail;
document.querySelector('#post_email').addEventListener('click', function() {
    let email = document.querySelector('#email').value;
    userEmail = email;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (email === '') {
        mostrarErro("Informe seu E-mail e tente novamente.");
        return;
    }

    if (!emailPattern.test(email)) {
        mostrarErro("Informe um e-mail válido.");
        return;
    }

    let jsonData = JSON.stringify({"email": email});

    fetch("http://127.0.0.1:8000/api/v1/verify-email/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: jsonData
    })
    .then(response => response.json())
    .then(data => {
        if (data['status_code'] === 201) {
            document.querySelector('.email').classList.add('transparent');
            document.querySelector('.form').classList.remove('transparent');
            document.querySelector('#nextButton1').classList.remove('transparent');
        } else if (data['status_code'] === 200) {
            document.querySelector('.email').classList.add('transparent');
            document.querySelector('.choices').classList.remove('transparent');
        }
    })
    .catch(error => {
        console.log(error);
    });
});

let formData = {};

document.querySelector('#nextButton1').addEventListener('click', function() {
    let q1 = document.querySelector('#sleep-hour').value;
    let q2 = document.querySelector('#time-to-sleep').value;
    let q3 = document.querySelector('#wakeup-hour').value;
    let q4 = document.querySelector('#slipping-time').value;

    if (q1 === '' || q2 === '' || q3 === '' || q4 === '') {
        mostrarErro('Preencha todos os campos para prosseguir.');
        return;
    }

    formData.question1 = q1;
    formData.question2 = q2;
    formData.question3 = q3;
    formData.question4 = q4;

    document.querySelector('#form1').classList.add('transparent');
    document.querySelector('#form2').classList.remove('transparent');
    document.querySelector('#nextButton1').classList.add('transparent');
    document.querySelector('#nextButton2').classList.remove('transparent');
});

document.querySelector('#nextButton2').addEventListener('click', function() {
    let q5a = document.querySelector('#\\35 a input:checked')?.id;
    let q5b = document.querySelector('#\\35 b input:checked')?.id;
    let q5c = document.querySelector('#\\35 c input:checked')?.id;
    let q5d = document.querySelector('#\\35 d input:checked')?.id;
    let q5e = document.querySelector('#\\35 e input:checked')?.id;
    let q5f = document.querySelector('#\\35 f input:checked')?.id;
    let q5g = document.querySelector('#\\35 g input:checked')?.id;
    let q5h = document.querySelector('#\\35 h input:checked')?.id;
    let q5i = document.querySelector('#\\35 i input:checked')?.id;

    if (!q5a || !q5b || !q5c || !q5d || !q5e || !q5f || !q5g || !q5h || !q5i) {
        mostrarErro('Preencha todos os campos para prosseguir.');
        return;
    }

    formData.question5A = q5a;
    formData.question5B = q5b;
    formData.question5C = q5c;
    formData.question5D = q5d;
    formData.question5E = q5e;
    formData.question5F = q5f;
    formData.question5G = q5g;
    formData.question5h = q5h;
    formData.question5i = q5i;
    formData.question5j = 0;
    formData.question5jTitle = null;

    if (document.querySelector('#other_reason').value !== '') {
        let q5j = document.querySelector('#\\35 j input:checked')?.id;
        let q5jTitle = document.querySelector('#other_reason').value;
        formData.question5j = q5j;
        formData.question5jTitle = q5jTitle;
    }

    document.querySelector('#form2').classList.add('transparent');
    document.querySelector('#form3').classList.remove('transparent');
    document.querySelector('#nextButton2').classList.add('transparent');
    document.querySelector('#sendButton').classList.remove('transparent');
});

document.querySelectorAll('.options input').forEach(function(input) {
    input.addEventListener('click', function() {
        let self = input;
        self.closest('.options').querySelectorAll('.text-label').forEach(function(label) {
            label.style.color = '#fff';
        });
        let label = self.closest('.option-wrapper').querySelector('.text-label');
        label.style.color = '#BB86FC';
    });
});

document.querySelector('#sendButton').addEventListener('click', function() {
    let q6 = document.querySelector('#q6 input:checked')?.id;
    let q7 = document.querySelector('#q7 input:checked')?.id;
    let q8 = document.querySelector('#q8 input:checked')?.id;
    let q9 = document.querySelector('#q9 input:checked')?.id;

    if (!q6 || !q7 || !q8 || !q9) {
        mostrarErro('Preencha todos os campos para prosseguir.');
        return;
    }

    formData.question6 = q6;
    formData.question7 = q7;
    formData.question8 = q8;
    formData.question9 = q9;
    formData.user = userEmail;

    fetch("http://127.0.0.1:8000/api/v1/forms/send/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.querySelector('.form').classList.add('transparent');
        document.querySelector('#sendButton').classList.add('transparent');
        document.querySelector('.result').classList.remove('transparent');

        let resultTitle = document.querySelector('.form_result h1');
        let resultEmoji = document.querySelector('.form_result p');

        if (data['total_score'] <= 5) {
            resultTitle.textContent = 'Boa qualidade do sono';
            resultEmoji.textContent = '😁';
        } else if (data['total_score'] > 5 && data['total_score'] <= 10) {
            resultTitle.textContent = 'Pobre qualidade do sono';
            resultEmoji.textContent = '😟';
        } else if (data['total_score'] > 10) {
            resultTitle.textContent = 'Presença de distúrbio do sono';
            resultEmoji.textContent = '😣';
        }
    })
    .catch(error => console.log(error));
});

document.querySelector('#backToMenu').addEventListener('click', function() {
    document.querySelectorAll('.result, #form3, #backToMenu').forEach(function(element) {
        element.classList.add('transparent');
    });
    
    document.querySelectorAll('.email, #post_email').forEach(function(element) {
        element.classList.remove('transparent');
    });

    document.querySelector('#email').value = '';
});

document.querySelector('#newForm').addEventListener('click', function() {
    document.querySelector('.choices').classList.add('transparent');
    document.querySelector('.form').classList.remove('transparent');
    document.querySelector('#nextButton1').classList.remove('transparent');
});

document.querySelector('#view').addEventListener('click', function() {
    document.querySelector('.choices').classList.add('transparent');
    document.querySelector('.history').classList.remove('transparent');

    fetch(`http://127.0.0.1:8000/api/v1/results/list/?email=${userEmail}`, {
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        createChart(data);
        createResult(data);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
});

document.querySelector('#backToMenu1').addEventListener('click', function(){
    document.querySelector('.history').classList.add('transparent');
    document.querySelector('.choices').classList.remove('transparent');
})
