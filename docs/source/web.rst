.. _web_toplevel:

==================
Web/HTTP Interface
==================

publish
=======

Publish a message to a channel.

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.
* ``channel_name``: The target channel.
* ``payload``: The json payload to publish

Optional Form Variables:
    
* ``originator``: The name of the user who will appear to do the publish

Returns json:

.. sourcecode:: javascript

    [ success (boolean) , details (object) ]


Example:

Client Requests URL:
    
.. sourcecode:: none

    /web/publish?security_token=yo&channel_name=testing&payload=[1, 2, "foo"]&originator=dictator


Server Replies:
    
.. sourcecode:: javascript
    
    [ true, {} ]

And the following frame is published to channel 'testing':

.. sourcecode:: javascript

    { "user": dictator, "payload": [1, 2, "foo"] }



subscribe
=========

Add a user to a channel.

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.
* ``channel_name``: The target channel.
* ``name``: The name of the target user.

Returns json:

.. sourcecode:: javascript

    [ success (boolean) , details (object) ]


Example:

Client Requests URL:
    
.. sourcecode:: none

    /web/subscribe?security_token=yo&channel_name=testing&user=mcarter


Server Replies:
    
.. sourcecode:: javascript
    
    [ true, {} ]

And the user "mcarter" is subscribed to the channel "testing".

unsubscribe
===========

Remove a user from a channel.

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.
* ``channel_name``: The target channel.
* ``name``: The name of the target user.

Returns json:

.. sourcecode:: javascript

    [ success (boolean) , details (object) ]


Example:

Client Requests URL:
    
.. sourcecode:: none

    /web/unsubscribe?security_token=yo&channel_name=testing&user=mcarter


Server Replies:
    
.. sourcecode:: javascript
    
    [ true, {} ]

And the user "mcarter" is unsubscribed from the channel "testing".


message
=======

Publish a message to a user.

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.
* ``sender_name``: The user name of the message sender.
* ``recipient_name``: The user name of the message recipient.
* ``payload``: The json payload to send

Returns json:

.. sourcecode:: javascript

    [ success (boolean) , details (object) ]


Example:

Client Requests URL:

.. sourcecode:: none

    /web/message?security_token=yo&sender_name=bob&recipient_name=joe&payload=[1, 2, "foo"]


Server Replies:

.. sourcecode:: javascript

    [ true, {} ]

And the following message frame is sent to user 'joe':

.. sourcecode:: javascript

    { "sender": "bob", "recipient": "joe", "payload": [1, 2, "foo"] }


get_channel_info
================

Returns all settings and attributes of a channel.

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.
* ``channel_name``: The target channel.

Returns json:

[ success (boolean) , details (object) ]

Example:

Client Requests URL:
    
.. sourcecode:: none

    /web/get_channel_info?security_token=yo&channel_name=testing


Server Replies:
    
.. sourcecode:: javascript
    
    [
        true, 
        {
            "name": "testing", 
            "options": {
                "anonymous": false, 
                "history": [
                    [
                        "SUBSCRIBE", 
                        {
                            "user": "mcarter"
                        }
                    ], 
                    [
                        "PUBLISH", 
                        {
                            "payload": "good day", 
                            "user": "mcarter"
                        }
                    ], 
                    [
                        "PUBLISH", 
                        {
                            "payload": "was gibt es?", 
                            "user": "mcarter"
                        }
                    ]
                ], 
                "history_duration": 0,
                "history_size": 5, 
                "moderated": false, 
                "moderated_publish": true, 
                "moderated_subscribe": true, 
                "moderated_unsubscribe": true, 
                "polling": {
                    "form": {}, 
                    "interval": 5, 
                    "mode": "", 
                    "originator": "", 
                    "url": ""
                }, 
                "presenceful": true, 
                "reflective": true
            }, 
            "subscribers": [
                "mcarter"
            ]
        }
    ]

set_channel_options
===================

Set the options on a channel. 

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.
* ``channel_name``: The target channel.

Optional Form Variables:

* ``anonymous``: json boolean
* ``history``: json list in the proper history format
* ``history_duration``: json integer
* ``history_size``: json integer
* ``moderated``: json boolean
* ``moderated_publish``: json boolean
* ``moderated_subscribe``: json boolean
* ``moderated_unsubscribe``: json boolean
* ``polling``: json object in the proper polling format
* ``presenceful``: json boolean
* ``reflective``: json boolean
* ``state``: json object

Example:
    
Client Requests URL:
    
.. sourcecode:: none

    /web/set_channel_options?security_token=yo&channel_name=testing&history_size=2&presenceful=true


Server Replies:
    
.. sourcecode:: javascript
    
    [ true, {} ]

The ``history_size`` of the channel is now `2`, and ``presenceful`` is `false`.

create_channel
==============

TODO

destroy_channel
===============

TODO


state_set_key
=============
Sets a key in a channel's state object. If the key already exists it is replaced, and if not it is created.

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.
* ``channel_name``: The target channel.

Optional Form Variables:

* ``key``: The target key in the state
* ``val``: any valid json structure; it will be the new value of the given key on the state

Example:
    
Client Requests URL:
    
.. sourcecode:: none

    /web/state_set_key?security_token=yo&channel_name=testing&key=score&val={ "mcarter": 5, "desmaj": 11 }


Server Replies:
    
.. sourcecode:: javascript
    
    [ true, {} ]

The ``state`` of the channel now contains the key "testing" with the value { "mcarter": 5, "desmaj": 11 }. An onState javascript callback will be issued to all subscribers; They will be able to access subscription.state.score.mcarter and will see the value 5.

state_delete_key
================

Removes a key from the state of a channel. If the key doesn't exist then nothing happens.

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.
* ``channel_name``: The target channel.

Optional Form Variables:

* ``key``: The target key in the state to delete

Example:
    
Client Requests URL:
    
.. sourcecode:: none

    /web/state_delete_key?security_token=yo&channel_name=testing&key=score

	
Server Replies:
    
.. sourcecode:: javascript
    
    [ true, {} ]

	
The ``state`` of the channel no longer contains the key "score". An onState callback will be issued to all subscribers.

set_config
==========

Update certain configuration parameters (mostly webhook related options) immediately without restarting hookbox.

Required Form variables:
    
* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.

Optional Form Variables:

* ``cbhost``: json string
* ``cbport``: json integer
* ``cbpath``: json string
* ``cb_connect``: json string
* ``cb_disconnect``: json string
* ``cb_create_channel``: json string
* ``cb_destroy_channel``: json string
* ``cb_subscribe``: json string
* ``cb_unsubscribe``: json string
* ``cb_publish``: json string
* ``cb_single_url``: json string
* ``admin_password``: json string
* ``webhook_secret``: json string
* ``api_security_token``: json string

Example:
    
Client Requests URL:
    
.. sourcecode:: none

    /web/state_delete_key?security_token=yo&cbhost="1.2.3.4&cbport=80

  
Server Replies:
    
.. sourcecode:: javascript
    
    [ true, {} ]


The callback host is now set to ``1.2.3.4`` and the port is now ``80``.


get_user_info
================

Returns all settings and attributes of a user.

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.
* ``user_name``: The target user.

Returns json:

[ success (boolean) , details (object) ]

Example:

Client Requests URL:

.. sourcecode:: none

    /web/get_user_info?security_token=yo&user_name=mcarter


Server Replies:


.. sourcecode:: javascript

    [
        true,
        {
            "channels": [
                "testing"
            ],
            "connections": [
                "467412414c294f1a9d1759ace01455d9"
            ],
            "name": "mcarter",
            "options": {
                "reflective": true,
                "moderated_message": true,
                "per_connection_subscriptions": false
            }
        }
    ]


set_user_options
===================

Set the options for a user.

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.
* ``user_name``: The target user.

Optional Form Variables:

* ``reflective``: json boolean - if true, private messages sent by this user will also be sent back to the user
* ``moderated_message``: json boolean - if true, private messages sent by this user will call the message webhook
* ``per_connection_subscriptions``: json boolean - if true, only the user connection (or connections) that sends a subscribe frame will be subscribed to the specified channel. Otherwise, all of a user's connections will share channel subscriptions established by any of the connections. 

Example:

Client Requests URL:

.. sourcecode:: none

    /web/set_user_options?security_token=yo&user_name=mcarter&reflective=false


Server Replies:

.. sourcecode:: javascript

    [ true, {} ]

The ``reflective`` of the user is now `false`.

get_server_info
================

Returns all current users and connections of the server.

Required Form Variables:

* ``security_token``: The password specified in the config as ``-r`` or ``--api-security-token``.

Returns json:

[ success (boolean) , details (object) ]

Example:

Client Requests URL:

.. sourcecode:: none

    /web/get_server_info?security_token=yo


Server Replies:


.. sourcecode:: javascript

    [
        true,
        {
            "channels": [
                "testing",
                "testing2"
            ],
            "connections": [
                "467412414c294f1a9d1759ace01455d9",
                "759ace01455d9467412414c294f1a9d1",
                "14c294f1a9d1759ace01455d94674124"
            ]
        }
    ]
