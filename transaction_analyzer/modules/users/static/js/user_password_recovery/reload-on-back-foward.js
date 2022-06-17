if (String(window.performance.getEntriesByType("navigation")[0].type) === "back_forward") {
    window.location.href = `${window.location.origin}/`;
}