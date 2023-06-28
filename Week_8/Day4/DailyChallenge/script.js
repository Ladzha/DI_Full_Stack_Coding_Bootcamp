// Daily Challenge : Creating Objects

// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.

// Create a class named Video. The class should be constructed with the following parameters:
// title (a string)
// uploader (a string, the person who uploaded it)
// time (a number, the duration of the video - in seconds)
// Create a method called watch() which displays a string as follows:
// “uploader parameter watched all time parameter of title parameter!”
// Instantiate a new Video instance and call the watch() method.
// Instantiate a second Video instance with different values.
// Bonus: Use an array to store data for five Video instances (ie. title, uploader, time)
// Think of the best data structure to save this information within the array.
// Bonus: Loop through the array to instantiate those instances.

class Video{
    constructor(title, uploader, time){
        this.title = title;
        this.uploaderPerson = uploader;
        this.duration = time;
    }

    watch(){
        console.log(`${this.uploaderPerson} watched all ${this.duration} minutes of ${this.title}!`);
    }
}

const catVideo = new Video('Cute cat', 'Sara', 3);

catVideo.watch();


const dogVideo = new Video('Cute dog', 'Lola', 5);

dogVideo.watch();

const data = [
{title: 'Tiger and kitty', uploader: 'John', time: 4},
{title: 'Colorful balloons', uploader: 'Fill', time: 2},
{title: 'Sunny day', uploader: 'Pitter', time: 6},
{title: 'Holidays', uploader: 'Gilbert', time: 3},
{title: 'Cute animals', uploader: 'Lily', time: 8}
];


class Video2{
    constructor(title, uploader, time){
        this.title = title;
        this.uploaderPerson = uploader;
        this.duration = time;
    }

    watch(){
        console.log(`${this.uploaderPerson} watched all ${this.duration} minutes of ${this.title}!`);
    }
}

for(const element of data){
    const video= new Video(element.title, element.uploader, element.time);
    video.watch();
}