---
uid: DevExpress.ExpressApp.TreeListEditors.Win.CategorizedListEditor
name: CategorizedListEditor
type: Class
summary: Represents a [List Editor](xref:113189) used to display categorized data.
syntax:
  content: 'public class CategorizedListEditor : GridListEditor'
seealso:
- linkId: DevExpress.ExpressApp.TreeListEditors.Win.CategorizedListEditor._members
  altText: CategorizedListEditor Members
- linkId: "113189"
---
List Editors are used by [List Views](xref:112611) to display object collections in a UI. The **CategorizedListEditor** is implemented in the [TreeList Editors module](xref:112841), and displays data in the form of a two-dimensional table accompanied by the category tree:

![CategorizedListEditor2](~/images/categorizedlisteditor2116348.png)

The **CategorizedListEditor** is an extension of the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor). As such, the **CategorizedListEditor** provides the same two-dimensional table data representation, just like the **GridListEditor**. However, the **CategorizedListEditor** has a couple of distinct features:

* It cannot display objects of any type. The **CategorizedListEditor** can only display objects of a type implementing the [](xref:DevExpress.Persistent.Base.General.ICategorizedItem) interface.
* It does not display all the existing objects at once. Only the objects that correspond to the currently selected category in the category tree are displayed in the grid.

The **CategorizedListEditor** operates with two collections:

1. The first collection is the object collection passed to the **CategorizedListEditor** by a List View that uses it as the [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor). Note that since these are **ICategorizedItem** objects, each object has the [ICategorizedItem.Category](xref:DevExpress.Persistent.Base.General.ICategorizedItem.Category) property. This property returns an [](xref:DevExpress.Persistent.Base.General.ITreeNode) category corresponding to the object.
2. The second collection is the categories collection created and managed solely by the **CategorizedListEditor**. This collection's objects are **ITreeNode** category objects, and they are used to build the category tree.

When the **CategorizedListEditor** must display objects in a UI, it builds the category tree. Note, that all existing categories are retrieved. So, even if the object collection passed to the **CategorizedListEditor** by the List View
does not contain objects corresponding to a particular category, this category will still be displayed in the category tree. The currently selected category in the category tree is used to create a filtering criterion. The filtering criterion is applied to the collection of the List View's Collection Source. So, only the objects that correspond to the currently selected category are displayed in the **CategorizedListEditor**'s grid. In essence, the category tree acts as a visual filter that allows end-users to filter the collection of the List View's Collection Source. This filter is the basic difference between the **CategorizedListEditor** and **GridListEditor**.

Since the **CategorizedListEditor** derives from the **GridListEditor**, all the **GridListEditor**'s features are supported. For a features overview, refer to the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) class description.

To display the category tree, the **ObjectTreeList** control is used. This control is a descendant of the [](xref:DevExpress.XtraTreeList.TreeList). You can access the category tree via the [CategorizedListEditor.CategoriesListView](xref:DevExpress.ExpressApp.TreeListEditors.Win.CategorizedListEditor.CategoriesListView) property, although it is not generally needed.

To learn how to implement the **ICategorizedItem** interface, refer to the [Categorized List](xref:112838) topic.

For additional information on the **CategorizedListEditor**, and an overview of the **TreeListEditors** module, refer to the [TreeList Editors Module Overview](xref:112836) topic.

> [!NOTE]
> * **CategorizedListEditor** supports only [Client](xref:118449)mode ([CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode)).
> * Categories with 'struct' key properties are not supported.