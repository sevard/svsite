// 
/**
 * Copies the contents of a textarea element to the clipboard.
 *
 * @param {string} textareaId - The ID of the textarea element whose content will be copied.
 */
function copyToClipboard(textareaId) {
    const textarea = document.getElementById(textareaId);

    if (textarea) {
        navigator.clipboard.writeText(textarea.value)
            .then(() => {

                const btn = document.getElementById('btn-' + textareaId);
                
                if (btn) {
                    const originalText = btn.textContent;
                    btn.textContent = 'Copied!';
                }

            })
            .catch(err => {
                // Fallback for browsers that do not support Clipboard API
                if (window.isSecureContext) {
                    console.error('Clipboard API not available:', err);
                } else {
                    console.error('Clipboard API requires a secure context (HTTPS).');
                }
            });
    }
}

function resetBtnText(btnId) {
    const btn = document.getElementById(btnId);
    if (btn) btn.textContent = "Copy";
}