<script>
// @ts-nocheck

  import { data } from "../shared.svelte";
  import { Icon } from 'svelte-icons-pack';
  import { BsDatabaseFill } from "svelte-icons-pack/bs";
  import { BsTable } from "svelte-icons-pack/bs";

  fetch('http://localhost:9999/api/dblist')
  .then((res) => res.json())
  .then((json) => data.dbs = json)
  .catch((e) => console.error(e))


  const tables = {}
  async function fetchTables(db) {
    try {
      const response = await fetch('http://localhost:9999/api/tables/' + db);
      const json = await response.json();
      tables[db] = json;
      data.selected = db;
    } catch(e) {
      console.log(e);
      alert('Error is occured.')
    }
  }
</script>

<ul class="dbs">
  {#each data.dbs as db}
  <li>
    <button on:click={() => fetchTables(db)}>
      <Icon src={BsDatabaseFill} size={16} />
      <span class={data.selected === db ? 'selected' : ''}>{db}</span>
    </button>
    {#if tables[db] !== undefined && tables[db] !== null}
    <ul class="tables">
      {#each tables[db] as tb}
      <li>
        <Icon src={BsTable} size={13} />
        <span>{tb}</span>
      </li>
      {/each}
    </ul>
    {/if}
  </li>
  {/each}
</ul>

<style lang="scss">
  ul.dbs {
    margin: 0;
    padding: 0;
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 10px;
    & li {
      color: #fff;
      & > button {
        border: 0;
        background: none;
        color: #fff;
        display: flex;
        gap: 5px;
        align-items: center;
        cursor: pointer;
        & > span.selected {
          font-weight: bold;
        }
      }
    }
  }

  ul.tables {
    list-style: none;
    margin: 5px 0 15px 28px;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 5px;
    & li {
      display: flex;
      gap: 5px;
      align-items: center;
    }
  }
</style>