$(function(){
    var ItemModel = function(data) {
        // Private variables
        var self = this;

        // Constructor
        ko.mapping.fromJS(data, {}, self);
    };

    var CategoryModel = function(data) {
        // Private variables
        var self = this;

        // Constructor
        ko.mapping.fromJS(data, {}, self);
    };

    var ModelView = function() {
        // Private variables
        var self = this;
        var socket = io.connect('/socketio');
        var mapping = {
            'categories': {
                create: function(data) {
                    return new CategoryModel(data.data);
                },
                key: function(data) {
                    return ko.unwrap(data.id);
                }
            },
            'items': {
                create: function(data) {
                    return new ItemModel(data.data);
                },
                key: function(data) {
                    return ko.unwrap(data.id);
                }
            }
        };

        // Constructor
        socket.on('categories', function(data) {
            ko.mapping.fromJS(data, mapping, self);
        });

        socket.on('items', function(data) {
            ko.mapping.fromJS(data, mapping, self);
        });

        socket.on('connect', function() {
            self.update();
        });

        // Public variables
        self.categories = ko.observableArray();
        self.items = ko.observableArray();

        // Public methods
        self.update = function() {
            socket.emit('get_categories', {});
            socket.emit('get_items', {});
        };

        self.removeItem = function(item) {
            if(confirm('Are you sure?')) {
                socket.emit('remove_item', {item_id: ko.unwrap(item.id)});
            }
        };

        self.removeCategory = function(category) {
            if(confirm('Are you sure?')) {
                socket.emit('remove_category', {category_id: ko.unwrap(category.id)});
            }
        };
    };

    ko.applyBindings(new ModelView(), $('#table')[0]);
});
