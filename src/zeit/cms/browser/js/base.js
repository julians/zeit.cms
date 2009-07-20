(function() {
    var declare_namespace = function(namespace) {
        var obj = window;
        forEach(namespace.split('.'), function(name) {
            if (isUndefined(obj[name])) {
                obj[name] = {}
            }
            obj = obj[name];
        });
    }
    declare_namespace('zeit.cms');
    zeit.cms.declare_namespace = declare_namespace;
})();


zeit.cms.ScrollStateRestorer = gocept.Class.extend({

    construct: function(content_element) {
        this.content_element = $(content_element);
    },

    connectWindowHandlers: function() {
        var othis = this;
        this.restoreScrollState();
        connect(window, 'onunload', function(event) {
            othis.rememberScrollState();
        });
        connect(this.content_element, 'initialload', function(event) {
            if (event.src() == othis.content_element) {
                othis.restoreScrollState();
            }
        });
    },

    rememberScrollState: function() {
        var position = this.content_element.scrollTop;
        var id = this.content_element.id;
        if (!id) {
            return;
        }
        zeit.cms.setCookie(id, position.toString(), null, '/');
     },

    restoreScrollState: function() {
        var id = this.content_element.id;
        if (!id) {
            return;
        }
        var position = zeit.cms.getCookie(id);
        this.content_element.scrollTop = position;
    },

});


zeit.cms.setCookie = function(name, value, expires, path, domain, secure) {   
  var val = escape(value);
  cookie = name + "=" + val +
    ((expires) ? "; expires=" + expires.toGMTString() : "") +
    ((path) ? "; path=" + path : "") +
    ((domain) ? "; domain=" + domain : "") +
    ((secure) ? "; secure" : "");
  document.cookie = cookie;
}

zeit.cms.getCookie = function(name) {
  var dc = document.cookie;
  var prefix = name + "=";
  var begin = dc.indexOf("; " + prefix);
  if (begin == -1) {
    begin = dc.indexOf(prefix);
    if (begin != 0) return null;
  } else {
    begin += 2;
  }
  var end = document.cookie.indexOf(";", begin);
  if (end == -1) {
    end = dc.length;
  }
  return unescape(dc.substring(begin + prefix.length, end));
}


    
zeit.cms.ClickOnceAction = gocept.Class.extend({

    construct: function(element) {
        var self = this;
        self.element = $(element);
        
        self.event_id = MochiKit.Signal.connect(
            self.element, 'onclick', self, 'disable');
    },

    disable: function() {
        var self = this;
        MochiKit.Signal.disconnect(self.event_id);
        MochiKit.Signal.connect(self.element, 'onclick', self, 'stop');
    },

    stop: function(event) {
        event.stop();
    },
});


zeit.cms.log_error = function(err) {
    /* the error can be either a normal error or wrapped
       by MochiKit in a GenericError in which case the message
       is the real error. We check whether the message is the real
       error first by checking whether its information is undefined.
       If it is undefined, we fall back on the outer error and display
       information about that */
    var real_error = err.message;
    if (isUndefinedOrNull(real_error.message)) {
        real_error = err;
    }
    console.trace();
    console.error(real_error.name + ': ' + real_error.message);
    return err;
};


zeit.cms._imported = {}
zeit.cms.import = function(src) {
    var d = new MochiKit.Async.Deferred();
    if (MochiKit.Base.isUndefined(zeit.cms._imported[src])) {
        var head = document.getElementsByTagName('head')[0]
        var script = MochiKit.DOM.createDOM('SCRIPT', {
            type: 'text/javascript',
            src: src});
        var ident = MochiKit.Signal.connect(script, 'onload', function() {
            MochiKit.Signal.disconnect(ident);
            d.callback();
        });
        head.appendChild(script);
        zeit.cms._imported[src] = true;
    } else {
        d.callback();
    }
    return d;
};