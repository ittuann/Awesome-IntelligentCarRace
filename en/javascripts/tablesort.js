document$.subscribe(function () {
  let tables = document.querySelectorAll("article table:not([class])");
  tables.forEach(function (table) {
    // 为自定义排序添加标签
    let headerCells = table.querySelectorAll("th");
    headerCells.forEach(function (cell) {
      if (cell.textContent.trim().includes("获奖")) {
        cell.setAttribute("data-sort-method", "award");
      }
    });

    // 自定义获奖等级排序
    const AWARD_ORDER = ["国1", "国2", "国3", "省1", "省2", "省3"];

    Tablesort.extend(
      "award",
      function (item) {
        return typeof item === "string" && AWARD_ORDER.includes(item);
      },
      function (a, b) {
        return AWARD_ORDER.indexOf(a) - AWARD_ORDER.indexOf(b);
      }
    );

    new Tablesort(table);
  });
});
