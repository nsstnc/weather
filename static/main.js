const url = window.location.href;
const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const resultsBox = document.getElementById('results-box');
const langBox = document.getElementById('lang');

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

// смена языка страницы
langBox.onclick = function() {

    const current_lang = langBox.innerHTML;

    $.ajax({
        type: 'POST',
        url: 'change_lang/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'current_lang': current_lang,
        }
        //ajax без ответа, нужен только, чтобы запустить функцию из views
    });

};

// выдача подходящих городов в поиске
const sendSearchData = (city) => {
    $.ajax({
        type: 'POST',
        url: 'search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'city': city,
        },
        success: (res) => {
            const data = res.data

            if (Array.isArray(data)) {
                resultsBox.innerHTML = ``
                data.forEach(item => {
                    resultsBox.innerHTML += `
                        <p><a href="#" id='${item.country_short}' class='item'>${item.city}, ${item.country}</a></p>`
                })
            } else {
                if (searchInput.value.length > 0) {
                    resultsBox.innerHTML = `<b>${data}</b>`
                }
            }
        },
        error: (err) => {
            console.log(err)
        }
    })
};

document.addEventListener('click', ({target: t}) => {
    if (t.matches('.item')) {
        document.querySelector('[id="search-input"]').value = t.innerText.split(',')[0] + ', ' + t.id;
        searchForm.submit();
    }
});

searchInput.addEventListener('keyup', e => {
    if (e.target.value.length >= 2) {
        if (resultsBox.classList.contains('not-visible')) {
            resultsBox.classList.remove('not-visible')
        }
        sendSearchData(e.target.value)
    } else {
        resultsBox.classList.add('not-visible')
    }
})



