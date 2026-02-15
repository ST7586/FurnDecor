function formatPrice(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function changeVariant(btn) {

    document.querySelectorAll('.seater-btn')
        .forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    document.getElementById("mainSofaImage").src = btn.dataset.image;

    document.querySelector('.new-price').innerText =
        "₹" + formatPrice(btn.dataset.price);

    document.querySelector('.old-price').innerText =
        "₹" + formatPrice(btn.dataset.old);
}

function toggleAcc(el) {
    const body = el.nextElementSibling;
    body.classList.toggle("open");
    el.querySelector("span").innerText =
        body.classList.contains("open") ? "-" : "+";
}

function increaseQty(btn) {
    let box = btn.closest(".qty-box");
    let qty = box.querySelector(".qtyValue");

    let val = parseInt(qty.textContent);
    qty.textContent = val + 1;
}

function decreaseQty(btn) {
    let box = btn.closest(".qty-box");
    let qty = box.querySelector(".qtyValue");

    let val = parseInt(qty.textContent);
    if (val > 1) {
        qty.textContent = val - 1;
    }
}


function toggleWishlist(productId) {
    fetch(`/wishlist/add/${productId}/`)
    .then(res => res.json())
    .then(data => {
        const btn = document.getElementById("wishlistBtn");

        if (data.added) {
            btn.classList.add("wish-active");
            btn.innerText = "♥";
        } else {
            btn.classList.remove("wish-active");
            btn.innerText = "♡";
        }

        // navbar count update
        document.querySelector(".nav-icons .count").innerText = data.count;

});
}


document.getElementById("wishlistToggle")?.addEventListener("click", function () {
    document.getElementById("wishlistPanel").classList.add("open");
});

document.getElementById("closeWishlist")?.addEventListener("click", function () {
    document.getElementById("wishlistPanel").classList.remove("open");
});


function removeFromWishlist(productId) {
    fetch(`/wishlist/add/${productId}/`)
    .then(res => res.json())
    .then(data => {

        // navbar count update
        document.querySelector(".nav-icons .count").innerText = data.count;

        // remove item from panel
        const item = document.getElementById(`wishlist-item-${productId}`);
        if (item) {
            item.remove();
        }

        // agar empty ho gaya
        const panel = document.getElementById("wishlistPanel");
        if (panel.querySelectorAll(".wishlist-item").length === 0) {
            panel.innerHTML += "<p>No items in wishlist</p>";
        }
    });
}


document.addEventListener("DOMContentLoaded", function () {
    const closeBtn = document.getElementById("closeWishlist");

    if (closeBtn) {
        closeBtn.addEventListener("click", function () {
            document.getElementById("wishlistPanel")
                .classList.remove("open");
        });
    }
});


function handleEmptyWishlist(panel) {
    if (panel.querySelectorAll(".wishlist-item").length === 0) {
        const emptyMsg = document.createElement("p");
        emptyMsg.innerText = "No items in wishlist";
        emptyMsg.classList.add("empty-wishlist");
        panel.appendChild(emptyMsg);
    }   
}

