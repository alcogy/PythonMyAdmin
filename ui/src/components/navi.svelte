<script>
  import { data } from "../shared.svelte";

  // TODO sample post query.
  async function enter() {
    try {
      const response = await fetch('http://localhost:9999/api/sql', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({'db': 'mossapi', 'sql': data.query})
    });
    const result = await response.json();
    data.data = result;
    } catch (e) {
      console.error(e);
      data.data = [];
      alert('error')
    } 
    
  }
</script>

<nav>
  <button on:click={enter}>Execute</button>
</nav>
  
<style lang="scss">
  nav {
    background-color: #ddd;
    height: 30px;
    display: flex;
    gap: 10px;
    align-items: center;
    padding: 0 4px;
  }
</style>