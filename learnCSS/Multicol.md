阅读笔记：当我们使用 Grid 和 Flexbox 时，Multicol 经常被忽略。[When And How To Use CSS Multi-Column Layout](https://www.smashingmagazine.com/2019/01/css-multiple-column-layout-multicol/) 阐述 Multicol 的独特之处，并展示了一些有用的模式和网站。

# Multicol（Multi Columns）

- Multicol 基本思想：像报纸一样，内容块多列展示。
- Multicol 容器中元素正常文档流。
- Flexbox（或 Grid）容器中元素参与 flex（或网格）布局。

# 容器元素样式属性
- `column-count` 属性指定内容块的列数。
- `column-width` 属性指定内容块的宽度，让浏览器确定适合的列数。
- `column-rule` 属性在内容列之间添加样式列，类似于 border。
- `column-gap` 属性控制内容列之间的间隙，该属性默认值 `1em`。

# 容器子元素样式属性
- `column-span` 属性跨列（Spanning Columns），目前规范参数 all 或 none 。
- 通过将 multicol 与其他布局方法相结合，实现跨越局部列显示。
- Multicol 控制内容中断位置属性 `page-break-`。  
注意：CSS Fragmentation 规范定义了为任何上下文设计的碎片属性 `break-`。

# 最佳实践

1. 折叠小UI或文本元素  
Multicol 可以在任何需要占用较少空间的项目列表的地方使用。  
例如，复选框的简单列表或名称列表。
2. 砌体（Masonry）类型的内容显示  
创建此类不等高项布局，Multicol 是唯一的布局方法，网格要么留下间隙，要么拉伸项目以形成严格的二维网格。
3. Grid 和 FLEXBOX 后备  
使用 `display: flex` 或 `display: grid` 将删除任何列行为，将该容器转换为Flex或Grid布局。  
不支持 Grid 和 FLEXBOX 的浏览器将获得 multicol 显示。