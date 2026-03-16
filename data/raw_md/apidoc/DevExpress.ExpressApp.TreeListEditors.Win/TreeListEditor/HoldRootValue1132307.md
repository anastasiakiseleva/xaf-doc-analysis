---
uid: DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor.HoldRootValue
name: HoldRootValue
type: Property
summary: Specifies whether the nodes whose parent node is absent in the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor)'s data source should be displayed as root.
syntax:
  content: public bool HoldRootValue { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the nodes whose parent node is absent in the data source are displayed as root; otherwise, **false**. The default value is **false**.'
seealso: []
---
This property affects what nodes are displayed in a [List View](xref:112611) represented by the **TreeListEditor**, when filtering the List View's [ListView.CollectionSource](xref:DevExpress.ExpressApp.ListView.CollectionSource). If the **HoldRootValue** property is set to **true**, then after a List View has been filtered so that some parent nodes are now missing, their first-level child nodes will be displayed as root. If the **HoldRootValue** property is set to **false**, the child nodes will not be displayed.