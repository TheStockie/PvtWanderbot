// Imports
require('dotenv').config();
const tmi = require('tmi.js');
const twitchParse = require('./twitchParse');

// Connection options
const opts = {
    options: { debug: false },
    connection: { reconnect: true },
    identity: {
        username: process.env.USERNAME,
        password: process.env.PASSWORD
    },
    channels: [
        process.env.CHANNELS
    ]
};

// Client creation
const client = new tmi.Client(opts);

// Register our event handlers (defined below)
client.on('message', onMessageHandler);
client.on('connected', onConnectedHandler);

client.connect();

// Message Handler
function onMessageHandler(target, context, msg, self){
    // Ignores messages sent by the own bot
    if (self) { return; }

    // Executes the parser script if the message starts with !
    else if (msg.charAt(0) === '!'){
        twitchParse.parseCommand(client, target, context, msg);
    }
}

// Logging connection
function onConnectedHandler(addr, port){
    console.log(`I have arrived at ${addr}:${port}`);
}