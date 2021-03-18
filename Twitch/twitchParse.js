// Imports
const tmi = require('tmi.js');

module.exports = {
    parseCommand: function(client, target, context, msg){
        // Removes whitespace from chat message
        let commandName = msg.trim().replace('!', '');
    
        exeCommand(client, target, context, commandName);
    }
};

// Commands list for the !commands command, command, command...
var commands = ["!hello, !discord, !commands, !join"];


// Command execution
function exeCommand(client, target, context, commandName){
    switch(commandName){

// -------------- COMMANDS -------------- \\
// To add simple text commands, follow this model:
//        case "commandName":
//            client.say(target, "Bot Message");
//            break;
//
// Add this BEFORE the default

        case "hello":
            client.say(target, "Hello!");
            break;

        case "discord":
            client.say(target, "Here's a link to my Discord Server: https://discord.gg/YuuRYWNfkC");
            break;

        case "commands":
            client.say(target, `Here are the commands: ${commands}`);
            break;

        case "join":
            break;

        default:
            break;
    }
}