import { Routes, Route } from "react-router-dom";
import Header from "./Header";
import BirdPage from "./BirdPage";
import BirdDetail from "./BirdDetail"

function App() {

  const API_URL="http://0.0.0.0:8080"


    return (
        <>
          <main>
            <Header />
            <Routes>
              <Route path="/:id" element={ <BirdDetail API_URL={API_URL}/> }/>
              <Route path="/" element={ <BirdPage  API_URL={API_URL}/> }/>
            </Routes>
          </main>
        </>
      );
}

export default App;
