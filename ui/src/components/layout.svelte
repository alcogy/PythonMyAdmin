<script>
// @ts-nocheck

  import Header from "./header.svelte";
  import Browser from "./browser.svelte";
  import Navi from "./navi.svelte";
  import Query from "./query.svelte";
  import Output from "./output.svelte";

  let pos = {
    x: 0,
    y: 0,
  };
  let width = 350;
  let height= 400;
  let isDownMouse = {
    side: false,
    content: false,
  };
  function mouseDownHandler(e) {
    if (this.getBoundingClientRect().width - e.offsetX < 4) {
      pos = {x: e.x, y: e.y};
      isDownMouse.side = true;
    }
  }

  function mouseDownContent(e) {
    if (this.getBoundingClientRect().height - e.offsetY < 4) {
      pos = {x: e.x, y: e.y};
      isDownMouse.content = true;
    }
  }
  
  document.addEventListener("mousemove", function(e) {
    if (isDownMouse.side) {
      width -= pos.x - e.x;
      if (width < 200) width = 200;
      pos.x = e.x;
    }

    if (isDownMouse.content) {
      height -= pos.y - e.y;
      if (height < 200) height = 200;
      pos.y = e.y;
    }
  });

  document.addEventListener("mouseup", function(e) {
    isDownMouse = {
      side: false,
      content: false,
    };
  });

</script>

<div class="wrap">
  <Header/>
  <main>
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div on:mousedown={mouseDownHandler} class="side" style="width: {width}px;">
      <div>
        <p class="side-caption">Browser</p>
      </div>
      <Browser />
    </div>
    <div class="f1">
      <div><Navi /></div>
      <!-- svelte-ignore a11y_no_static_element_interactions -->
      <div class="content-top" on:mousedown={mouseDownContent} style="height: {height}px;">
        <Query />
      </div>
      <div class="content-under">
        <Output />
      </div>
    </div>
  </main>
</div>

<style lang="scss">
  .wrap {
    width: 100vw;
    height: 100vh;
    overflow: auto;
    display: flex;
    flex-direction: column; 
    align-content: stretch;
  }
  main {
    height: 100%;
    display: flex;
    background-color: #222;
  }
  main div.f1 {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-content: stretch;
  }
  main > div.side {
    position: relative;
    padding: 10px;
    height: 100%;
    &::after {
      content: '';
      width: 4px;
      display: block;
      position: absolute;
      right: 0;
      top: 0;
      height: 100%;
      background-color: #ddd;
      cursor: ew-resize;
    }
  }
  main div.content-top {
    position: relative;
    &::after {
      content: '';
      width: 100%;
      display: block;
      position: absolute;
      left: 0;
      bottom: 0;
      height: 4px;
      background-color: #ddd;
      cursor: ns-resize;
    }
  }
  .side-caption {
    color: #fff;
    font-weight: bold;
    font-size: 1.2rem;
    margin: 0 0 10px 0;
  }
  .content-under {
    flex: 1;
    overflow: auto;
    contain: size;
  }
</style>