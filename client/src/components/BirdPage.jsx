import { useEffect, useState } from "react";
import NewBirdForm from "./NewBirdForm";
import BirdList from "./BirdList";
import Search from "./Search";

function BirdPage({API_URL}) {
  const [birds, setBirds] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    fetch(`${API_URL}/birds`)
      .then((r) => r.json())
      .then((birdsArray) => {
        setBirds(birdsArray);
      });
  }, []);

  function handleAddBird(newBird) {
    const updatedBirdsArray = [...birds, newBird];
    setBirds(updatedBirdsArray);
  }

  const displayedBirds = birds.filter((bird) => {
    return bird.name.toLowerCase().includes(searchTerm.toLowerCase());
  });

if(!birds) return <h1>...loading</h1>

  return (
    <main>
      <NewBirdForm onAddBird={handleAddBird} API_URL={API_URL}/>
      <Search searchTerm={searchTerm} onSearchChange={setSearchTerm} API_URL={API_URL}/>
      <BirdList birds={displayedBirds} API_URL={API_URL}/>
    </main>
  );
}

export default BirdPage;
