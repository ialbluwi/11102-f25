
function toggleExpandableCode(codeId, headerEl) {
    const codeContent = document.getElementById(codeId);
    const toggleBtn = headerEl.querySelector('.expandable-toggle-btn');
    const label = toggleBtn.querySelector('.expandable-label');

    if (codeContent.classList.contains('expanded')) {
        codeContent.classList.remove('expanded');
        toggleBtn.classList.remove('expanded'); // rotates arrow down
        if (label) label.textContent = 'Expand';
    } else {
        codeContent.classList.add('expanded');
        toggleBtn.classList.add('expanded'); // rotates arrow up
        if (label) label.textContent = 'Collapse';
    }
}



function copyExpandableCode(elementId, buttonElement) {
    const codeElement = document.getElementById(elementId);
    const text = codeElement.textContent;

    navigator.clipboard.writeText(text).then(function() {
        const originalText = buttonElement.textContent;
        buttonElement.textContent = 'Copied! ✓';

        setTimeout(() => {
            buttonElement.textContent = originalText;
            buttonElement.style.background = '';
        }, 2000);
    }).catch(function(err) {
        console.error('Could not copy text: ', err);
        alert('Failed to copy code');
    });
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('Expandable code blocks initialized');
});
