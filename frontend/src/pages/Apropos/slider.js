import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import img1 from "./assets/e.jpg";
import img2 from "./assets/PXL_20230128_122548192.jpg";
import img3 from "./assets/PXL_20230128_131948658.PORTRAIT.jpg";
import img4 from "./assets/PXL_20230204_123722959.jpg";
import styled from "styled-components";

const data = [
  {
    id: 1,
    img: img1,
    description: "La rencontre des étudiants du club GDSC UCB",
  },
  {
    id: 2,
    img: img2,
    description: "La rencontre des étudiants du club GDSC UCB",
  },
  {
    id: 3,
    img: img3,
    description: "La rencontre des étudiants du club GDSC UCB",
  },
  {
    id: 4,
    img: img4,
    description: "Ensemble pour l'innovation de notre pays",
  },
];

const SliderComponent = () => {
  const settings = {
    dots: true,
    infinite: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    autoplay: true,
    speed: 2000,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          initialSlide: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  };
  return (
    <Slider {...settings}>
      {data.map((carte, index) => (
        <CardRender className="slide" key={index}>
          <img src={carte.img} alt={`Slide ${index}`} className="img_carte" />
        </CardRender>
      ))}
    </Slider>
  );
};

export default SliderComponent;

const CardRender = styled.div`
  width: 100%;
  position: relative;
  border-radius: 15px;
  overflow: hidden;
  padding: 10px;

  img {
    width: 100%;
    border-radius: 15px;
  }
`;
