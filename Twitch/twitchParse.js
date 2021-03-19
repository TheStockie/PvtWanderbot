// Imports
const tmi = require('tmi.js');

const {exec} = require('child_process');

module.exports = {
    parseCommand: function(client, target, context, msg){
        // Removes whitespace from chat message
        let commandName = msg.trim().replace('!', '').split(' ');
    
        exeCommand(client, target, context, commandName);
    }
};

// Commands list for the !commands command, command, command...
var commands = ["!hello, !discord, !commands, !join"];


// Command execution
function exeCommand(client, target, context, parsedCommand){
    switch(parsedCommand[0]){

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
            exePython('join', client, context, target);
            // exePython(`python ../FLDB/parseFLDB.py join ${context['user-id']}`, client, context, target, commandName[0]);
            break;

        case "balance":
            exePython('balance', client, context, target);
            // exePython(`python ../FLDB/parseFLDB.py balance ${context['user-id']}`, client, context, target, commandName[0]);
            break;

        default:
            break;
    }
}

function exePython(command, client, context, target){
    switch(command){
        case 'join':
            exec(`python ../FLDB/parseFLDB.py join ${context['user-id']}`, (error, stdout, stderr) => {
                if (error) {
                    console.log(`error: ${error.message}`);
                    return;
                } 
                if (stderr) {
                    console.log(`stderr: ${stderr}`);
                    return;
                }

                if(stdout == 1){
                    client.say(target, `You\'ve been signed into FLDB. Welcome @${context['username']}!`)
                } else{
                    client.say(target, `You\'re already signed into FLDB, @${context['username']}. Silly goose!`)
                }
            });
            break;

        case 'balance':
            exec(`python ../FLDB/parseFLDB.py balance ${context['user-id']}`, (error, stdout, stderr) => {
                if (error) {
                    console.log(`error: ${error.message}`);
                    return;
                } 
                if (stderr) {
                    console.log(`stderr: ${stderr}`);
                    return;
                }
                result = stdout.replace('[','').replace(']','').split(', ');
                
                if(result[1] == 1){
                    client.say(target, `@${context['username']}, your balance is: ${result[0]} FLBux`)
                } else{
                    client.say(target, `You\'re not signed in @${context['username']}! Try !join`)
                }
            });
            break;
    }
}