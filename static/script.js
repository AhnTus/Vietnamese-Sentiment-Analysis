document.addEventListener('DOMContentLoaded', function() {
    // Auto-complete for comment input
    const commentInput = document.querySelector('textarea[name="comment_input"]');
    
    if (commentInput) {
        let generatedText = '';
        let tabPressed = false;

        commentInput.addEventListener('keydown', function(event) {
            if (event.key === 'Tab') {
                event.preventDefault();
                tabPressed = true;
            } else if (event.key === ' ') {
                tabPressed = false;
            }
        });

        commentInput.addEventListener('keyup', function(event) {
            if (event.key === 'Tab' && tabPressed) {
                event.preventDefault();
                let comment = commentInput.value.trim();
                fetch('/generate_text', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams({ comment: comment })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.generated_text) {
                        generatedText = data.generated_text;
                        commentInput.value += generatedText;
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        });
    }

    // Pagination for phone list
    const phoneList = document.querySelector('.phone-list');
    const items = document.querySelectorAll('.phone-item');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (phoneList && items.length > 0) {
        let currentIndex = 0;
        const itemsPerPage = 5;

        function showItems() {
            items.forEach((item, index) => {
                item.style.display = (index >= currentIndex && index < currentIndex + itemsPerPage) ? 'block' : 'none';
            });
        }

        prevBtn.addEventListener('click', function() {
            currentIndex = (currentIndex - itemsPerPage + items.length) % items.length;
            showItems();
        });

        nextBtn.addEventListener('click', function() {
            currentIndex = (currentIndex + itemsPerPage) % items.length;
            showItems();
        });

        showItems();
    }
});
