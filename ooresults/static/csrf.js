/*
 * Adds the header "X-Requested-With: XMLHttpRequest" to all requests sent
 * with XMLHttpRequest that change data (all methods except GET and HEAD).
 * The server rejects such requests without this header to protect against
 * cross-site request forgery (CSRF).
 */
(function () {
    const open = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function (method, ...args) {
        open.call(this, method, ...args);
        const m = String(method).toUpperCase();
        if (m !== "GET" && m !== "HEAD") {
            this.setRequestHeader("X-Requested-With", "XMLHttpRequest");
        }
    };
})();
