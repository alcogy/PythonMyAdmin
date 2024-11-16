<table>
  <thead>
    <tr>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>city</th>
      <th>language</th>
      <th>hobby</th>
      <th>created_at</th>
      <th>update_at</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>123909</td>
      <td>Jho Syme</td>
      <td>43</td>
      <td>Dublin</td>
      <td> Swift, OCaml, Go, TypeScript</td>
      <td>Guiness!!</td>
      <td>2024-11-12T11:34:20.003</td>
      <td>2024-11-12T11:34:20.003</td>
    </tr>
    <tr>
      <td>320232</td>
      <td>Steave Rosso</td>
      <td>55</td>
      <td>London</td>
      <td>C/C++, Rust, Kotlin, Haskell</td>
      <td>Guiness!!</td>
      <td>2024-11-12T11:34:20.003</td>
      <td>2024-11-12T11:34:20.003</td>
    </tr>
  </tbody>
</table>

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
      font-size: 1.0rem;
      white-space: nowrap;
    }
  }
</style>