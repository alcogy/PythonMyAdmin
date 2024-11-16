<script>
  let val = "";
  
  // TODO sample post query.
  async function enter() {
    console.log(val);
    const response = await fetch('http://localhost:9999/api/sql', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({'sql': val})
    });
    const data = await response.json();
    console.log(data);
  }
  
</script>

<button on:click={enter}>koko</button>
<textarea bind:value={val}></textarea>

<style lang="scss">
  textarea {
    resize: none;
    width: 100%;
    height: 100%;
    margin: 0;
    display: block;
    border: 0;
    padding: 5px;
    background-color: #353535;
    font-size: 15px;
    color: #fff;
    &:focus {
      outline: none;
    }
  }
</style>