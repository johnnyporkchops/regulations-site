define("definition-view",["jquery","underscore","backbone","regs-view","regs-data","regs-dispatch","regs-helpers"],function(e,t,n,r,i,s,o){var u=r.extend({className:"open-definition",events:{},render:function(){s.once("definition:callRemove",this.remove,this);var t=this.$el.find(".inline-interpretation"),n=this.$el.find("dfn.key-term"),r="#"+this.model.id,i="Go to definition in § "+this.model.id,u="continue-link",a=o.fastLink(r,i,u),f,l,c,h,p;this.$el.append(a),typeof t[0]!="undefined"&&(h=e(t[0]).data("interpFor"),this.$el.find(".inline-interpretation").remove(),f="#"+h,l="Go to related interpretations",c=o.fastLink(f,l,u),this.$el.append(c));if(typeof n[0]!="undefined"){p=n.length;for(var d=0;d<p;d++)e(n[d]).remove()}return s.trigger("definition:render",this.$el),this},remove:function(){return this.stopListening(),this.$el.remove(),s.trigger("definition:remove"),this}});return u});