<script>
  import { data } from '../shared.svelte'
</script>

{#if data.data !== undefined && data.data !== null}
<table>
  <thead>
    <tr>
      {#each data.data[0] as h}
      <th>{h}</th>
      {/each}
    </tr>
  </thead>
  <tbody>
    {#each data.data.slice(1) as columns}
    <tr>
      {#each columns as col}
      <td>{col}</td>
      {/each}
    </tr>
    {/each}
  </tbody>
</table>
{/if}

<style lang="scss">
  table {
    border-collapse: collapse;
    border-spacing: 0;
    padding: 0;
    & thead {
      position: sticky;
      top: 0;
      padding: 0;
      background-color: #444;
      z-index: 1;
    }
    & th {
      color: #fff;
      text-align: left;
      padding: 5px;
      border: 1px solid #666;
      font-weight: 500;
      font-size: 1.1rem;
    }
    & td {
      border: 1px solid #888;
      padding: 3px 5px;
      color: #fff;
      white-space: nowrap;
    }
  }
</style>