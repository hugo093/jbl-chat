function autoResizeTextarea(el) {
    el.style.height = 'auto'; // Reset the height
    el.style.height = Math.min(el.scrollHeight, 150) + 'px'; // Set to scroll height
}

function debounce(fn, delay = 300) {
    let timeout;
    return function (...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => fn.apply(this, args), delay);
    };
}

const debouncedResize = debounce(function (event) {
    if (event.target.classList.contains('autoresize')) {
        autoResizeTextarea(event.target);
    }
}, 100); // 100ms debounce

document.addEventListener('input', debouncedResize);