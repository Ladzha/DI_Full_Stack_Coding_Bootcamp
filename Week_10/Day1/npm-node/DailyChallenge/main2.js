// import date from 'date-and-time'

// const date = require('date-and-time')

const largeNumber = 356;

function getDateTime(){
    const now = new Date();
    console.log(`Data and time now ${now}`)
    return now
}
getDateTime()

module.exports = {largeNumber, getDateTime}; 
