import React from "react";
import styled from "styled-components";
import { Articles } from "./data/Article";
import CardArticle from "./component/CardArticle";
import Article from "../../components/Article";
import { useLocation } from "react-router-dom";
import { useEffect } from "react";
import axios from "axios";
export default function Sexualite() {
  const { pathname } = useLocation();
  const t = pathname.split("/")[1];
  const [OpenArtcticle, SetOpen] = React.useState(false);
  const [ArticleDetail, setArtcileDetaille] = React.useState([]);

  const OuvrirArtcle = (cle) => {
    console.log(Articles[1]);
    SetOpen(true);
    setArtcileDetaille(Articles[cle]);
  };
  const CloseArtcticle = () => {
    SetOpen(!OpenArtcticle);
  };

  useEffect(() => {
    window.scrollTo(0, 0);
    axios
      .get("https://apisosdoc.herokuapp.com/api/articles")
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  });
  return (
    <Sexualites>
      {OpenArtcticle ? (
        <Article Article={ArticleDetail} CloseArtcticle={CloseArtcticle} />
      ) : (
        <div className="Container">
          <div className="header">
            <h2>Sexualité</h2>
            <p>
              Besoin d'apprendre beaucoup plus sur la santé sexuelle ? Retrouvez
              tous les articles conçus par les experts ici
            </p>
          </div>

          <div className="ArticlesContainer">
            {Articles.map((Article, index) => (
              <CardArticle
                Article={Article}
                key={index}
                handleClick={() => OuvrirArtcle(index)}
              />
            ))}
          </div>
        </div>
      )}
      {/* {OpenArtcticle ? (
        <Article Article={ArticleDetail} CloseArtcticle={CloseArtcticle} />
      ) : null} */}
    </Sexualites>
  );
}
const Sexualites = styled.div`
  display: flex;
  width: 100%;
  min-height: 90vh;
  justify-content: center;
  gap: 10px;
  background: rgba(100, 166, 236, 0.1);

  animation: showing 0.3s ease-in;
  @keyframes showing {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }
  .Container {
    width: 80%;
    display: flex;
    padding-bottom: 1rem;
    flex-direction: column;

    @media screen and (max-width: 768px) {
      width: 100%;
    }

    .header {
      display: flex;
      flex-direction: column;
      text-align: center;

      h2 {
        font-style: normal;
        font-weight: 700;
        font-size: 40px;
        line-height: 60px;
        color: #39c3f6;
        padding: 0;

        @media screen and (max-width: 578px) {
          font-size: 32px;
        }
      }
      p {
        width: 90%;
        margin: auto;
        font-style: normal;
        font-weight: 400;
        font-size: 16px;
        line-height: 24px;
      }
    }

    .ArticlesContainer {
      display: flex;
      padding-top: 30px;
      gap: 25px;
      flex-wrap: wrap;
      justify-content: center;
    }
  }
`;
