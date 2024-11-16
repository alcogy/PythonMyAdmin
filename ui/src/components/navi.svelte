<nav>
  <span>one</span>
  <span>two</span>
  <span>three</span>
  <span>four</span>
</nav>
  
<style lang="scss">
  nav {
    background-color: #ddd;
    height: 30px;
    display: flex;
    gap: 10px;
    align-items: center;
    padding: 0 4px;
    & span {
      color: #333;
      padding: 0 5px;
    }
  }
</style>