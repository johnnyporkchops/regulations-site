define("header-view",["jquery","underscore","backbone","regs-dispatch"],function(e,t,n,r){var i=n.View.extend({el:".reg-header",initialize:function(){this.$activeEls=e("#menu, #site-header, #reg-content"),this.$tocLinks=e(".toc-nav-link")},events:{"click .toc-toggle":"openTOC","click .toc-nav-link":"toggleDrawer"},openTOC:function(t){t.preventDefault();var n=e(t.target),i=n.hasClass("open")?"close":"open";typeof this.$activeEls!="undefined"&&(r.trigger("toc:toggle",i+" toc"),n.toggleClass("open"),this.$activeEls.toggleClass("active"))},toggleDrawer:function(n){n.preventDefault();var i=e(n.target),s=t.last(i.attr("href").split("#"));this.$tocLinks.removeClass("current"),i.addClass("current"),r.trigger("drawer:stateChange",s)}});return i});