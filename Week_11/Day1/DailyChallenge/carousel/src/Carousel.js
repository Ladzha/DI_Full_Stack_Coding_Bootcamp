import './Carousel.css'
import React from 'react';
import ReactDOM from 'react-dom';
// import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from 'react-responsive-carousel';


// const Carousel = (props)=>{
//     const imgUrl1 = 'https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/jrfyzvgzvhs1iylduuhj.jpg'
//     const imgUrl2 ='https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/c1cklkyp6ms02tougufx.webp'
//     const imgUrl3 ='https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/e8fnw35p6zgusq218foj.webp'
//     const imgUrl4 ='https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/liw377az16sxmp9a6ylg.webp'

//     return(
//         <div>

//             HJK
//         <h1 class='label'>Hello</h1>
//         <img src={imgUrl1}/>
//         <img src={imgUrl2}/>
//         <img src={imgUrl3}/>
//         <img src={imgUrl4}/>

//         </div>
//     )
// }



class DemoCarousel extends React.Component {
    render() {
        return (
            <Carousel>
                <div>
                    <img src="assets/1.jpeg" />
                    <p className="legend">Legend 1</p>
                </div>
                <div>
                    <img src="assets/2.jpeg" />
                    <p className="legend">Legend 2</p>
                </div>
                <div>
                    <img src="assets/3.jpeg" />
                    <p className="legend">Legend 3</p>
                </div>
            </Carousel>
        );
    }
});

ReactDOM.render(<DemoCarousel />, document.querySelector('.demo-carousel'));

export default Carousel