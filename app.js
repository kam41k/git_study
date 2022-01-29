'use strict';


let fitlerPopup = document.querySelector('.filterPopup');
let fitlerLabel = document.querySelector('.filterLabel');
let filterIcon = document.querySelector('.filterIcon');

fitlerLabel.addEventListener('click', function() {
    fitlerPopup.classList.toggle('hidden');
    fitlerLabel.classList.toggle('filterLabelPink');
    filterIcon.classList.toggle('filterIconPink');

    if (filterIcon.getAttribute('src') === 'images/filter.svg') {
        filterIcon.setAttribute('src', 'images/filterHover.svg')
    } else {
        filterIcon.setAttribute('src', 'images/filter.svg')
    }
});

let filterHeaders = document.querySelectorAll('.filterCategoryHeader');
filterHeaders.forEach(function(header) {
    header.addEventListener('click', function(event) {
        event.target.nextElementSibling.classList.toggle('hidden');
    })
});

let filterSizes = document.querySelector('.filterSizes');
let filterSizeWrap = document.querySelector('.filterSizeWrap');
filterSizeWrap.addEventListener('click', function() {
    filterSizes.classList.toggle('hidden');
});

const cartIconCounter = document.querySelector('.cartIconWrap').querySelector('span');
const featuredItemsContainer = document.querySelector('.featuredItems');

document.querySelector('.cartIconWrap').addEventListener('click', () => {
  document.querySelector('.basket').classList.toggle('hidden');
})

featuredItemsContainer.addEventListener('click', event => {
    if (event.target.tagName === 'BUTTON') {
        cartIconCounter.textContent = `${+cartIconCounter.textContent + 1}`;
        const featuredDataElement = event.target.parentNode.parentNode.parentNode.querySelector('.featuredData');
        const price = Number.parseFloat(featuredDataElement
            .querySelector('.featuredPrice').textContent.trim().substring(1)).toFixed(2);
        const prodId = featuredDataElement.dataset.productId;
        const basket = document.querySelector('.basket');
        const basketTotalRow = basket.querySelector('.basketTotal');
        if (basket.dataset.productsInCart.includes(prodId)) {
            const product = basket.querySelector(`.prod${prodId}`);
            product.querySelector('.quant').textContent = `${
                +product.querySelector('.quant').textContent + 1
            }`;
            product.querySelector('.total').textContent = `$${
                (+product.querySelector('.quant').textContent * price).toFixed(2)
            }`;
        } else if (!basket.dataset.productsInCart.includes(prodId)) {
            basket.dataset.productsInCart += ` ${prodId}`;
            const newProduct = document.createElement('div');
            newProduct.classList.add('basketRow',`prod${prodId}`);
            newProduct.innerHTML = `<div>${featuredDataElement.querySelector('.featuredName').textContent}</div>
<div class="quant">1</div>
<div>$${price}</div>
<div class="total">$${price}</div>`
            basketTotalRow.before(newProduct);
        }
        const basketRows = basket.querySelectorAll('.basketRow');
        let total = 0;
        for (let i = 1; i < basketRows.length; i++) {
            total += +basketRows[i].querySelector('.total').textContent.substring(1);
        }
        basketTotalRow.querySelector('.basketTotalValue').textContent = `${total.toFixed(2)}`;
    }
})