var btn = document.getElementById('cardBtn');

btn.addEventListener('click', function() {
    var card = document.getElementById('debitcard');
    card.classList.toggle('cardNone');
});
