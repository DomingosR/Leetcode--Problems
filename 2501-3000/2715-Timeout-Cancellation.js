var cancellable = function(fn, args, t) {
    auxTimeout = setTimeout(fn, t, ...args);
    return () => clearTimeout(auxTimeout);
};