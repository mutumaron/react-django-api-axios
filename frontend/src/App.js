import axios from "axios";
// import React from 'react';

// class App extends React.Component {
//   state = { details: [], }

//   componentDidMount() {
//     let data;
//     axios
//       .get("http://localhost:8000/api")
//       .then(res => {
//         data = res.data;
//         this.setState({
//           details: data,
//         });
//       })
//       .catch((err) => {});
//   }

//   render() {
//     return (
//       <div>
//         <header>Data Generated From Django</header>
//         <hr />
//         {this.state.details.map((output) => (
//           <div key={output.id}>
//             <h2>{output.name}</h2>
//             <h3>{output.school}</h3>
//             <h3>{output.message}</h3>
//           </div>
//         ))}
//       </div>
//     );
//   }
// }

import React, { useState, useEffect } from 'react';

const App = () => {
  const [details, setDetails] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8000/api");  // Update the URL to your actual endpoint
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        const data = await response.json();
        setDetails(data);
      } catch (error) {
        // Handle error
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []); // Empty dependency array means the effect runs once after the initial render

  return (
    <div>
      <header>Data Generated From Django</header>
      <hr />
      {details.map((output) => (
        <div key={output.id}>
          <h2>{output.name}</h2>
          <h3>{output.school}</h3>
          <h3>{output.message}</h3>
        </div>
      ))}
    </div>
  );
};

export default App;


// export default App;
