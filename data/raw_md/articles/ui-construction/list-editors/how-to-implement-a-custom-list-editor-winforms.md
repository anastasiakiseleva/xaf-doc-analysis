---
uid: "112659"
seealso:
- linkId: "112607"
- linkId: "112611"
- linkId: "402154"
- linkId: "112820"
- linkId: "403258"
- linkId: DevExpress.ExpressApp.Editors.IComplexListEditor
title: 'How to: Implement a Custom List Editor (WinForms)'
---
# How to: Implement a Custom List Editor (WinForms)

The **XAF** is shipped with a number of [built-in List Editors](xref:113189). However, in certain scenarios you may need to implement a custom List Editor, to display object collections in a particular way. This topic demonstrates how to implement a custom **WinCustomListEditor** List Editor that uses a control from the .NET Framework library. This List Editor is designed to display objects, implementing a custom **IPictureItem** interface as a list of images, one for each object. It can be used, for instance, to display DVD covers.

The following image demonstrates the implemented List Editor in an Album List View:

![WinThumbnailEditor](~/images/winthumbnaileditor115389.png)

> [!NOTE]
> You can see the code implemented here in the **FeatureCenter** Demo installed with **XAF**. This demo is located in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder, by default.

> [!TIP]
> To learn how to support a context menu for the **WinCustomListEditor**, refer to the [How to: Support a Context Menu for a Custom WinForms List Editor](xref:112660) topic.

When implementing a custom List Editor that works with specific data, you can design it for a particular class. However, in this example, an interface will be introduced containing the properties required by the List Editor. Then, the List Editor will be designed to display objects implementing the interface. This approach allows you to simultaneously use that same List Editor for different classes. List Views displayed using the **WinCustomListEditor** will have two columns: **Image** and **Text**. The special interface has an additional **ID** property that represents a unique object identifier.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
//...
interface IPictureItem {
    Image Image { get; }
    string Text { get; }
    string ID { get; }
}
```
***

Start implementing the List Editor by inheriting its class from the [](xref:DevExpress.ExpressApp.Editors.ListEditor) class, and implement basic functionality by overriding the following members. [!include[PublicEditor](~/templates/publiceditor111797.md)]

* **CreateControlsCore** method, that instantiates the List Editor's control. Override it to create and configure the control.
* **AssignDataSourceToControl** method, that assigns the List Editor's data source to its control. Override it to support object change notification, when the data source implements the **IBindingList** interface.
* [ListEditor.Refresh](xref:DevExpress.ExpressApp.Editors.ListEditor.Refresh) method, that refreshes data in the List Editor's control. Override it to make the control reload all objects from its data source.
* [ListEditor.Dispose](xref:DevExpress.ExpressApp.Editors.ListEditor.Dispose) method, that disposes of a manually allocated **controlDataSource** property .
* To specify that List Views displaying **IPictureItem**, objects should use the **WinCustomListEditor**, decorate the List Editor class with the [](xref:DevExpress.ExpressApp.Editors.ListEditorAttribute).

The demonstrated List Editor can display a collection of objects implementing the **IPictureItem** interface. However, it does not support items selection, because it cannot recognize what item is currently selected. To support selection, the following members must be modified:

* In the **CreateControlsCore** method, subscribe to the control's **SelectedIndexChanged** and **ItemSelectionChanged** events. In the **SelectedIndexChanged** event handler, call the **OnSelectionChanged** method. In the **ItemSelectionChanged** event handler, call the **OnSelectionChanged** and **OnFocusedObjectChanged** methods.
* Override the [ListEditor.SelectionType](xref:DevExpress.ExpressApp.Editors.ListEditor.SelectionType) property. Since the **ListView** control supports both single and multiple selections, this property must return [SelectionType.Full](xref:DevExpress.ExpressApp.SelectionType.Full).
* Override the [ListEditor.GetSelectedObjects](xref:DevExpress.ExpressApp.Editors.ListEditor.GetSelectedObjects) method. This method must return a list of the selected objects.

In addition to selection, a List Editor should be able to invoke a Detail View for the focused object when an end-user presses ENTER, or double-clicks the object. For this purpose, modify the following members:

* In the **CreateControlsCore** method, subscribe to the control's **MouseDoubleClick** and **KeyDown** events. In the event handlers, call the **OnProcessSelectedItem** method.
* Override the [ListEditor.FocusedObject](xref:DevExpress.ExpressApp.Editors.ListEditor.FocusedObject) property, to get and set the focused object. To do this, we implement an additional **FindByTag** helper method.
* Modify the [ListEditor.Refresh](xref:DevExpress.ExpressApp.Editors.ListEditor.Refresh) method, to make the List Editor retain focus when refreshing data in the control.

To support [navigation](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController) in your custom List Editor for non-client modes, implement the `IControlOrderProvider` interface.

If you need to store the editor settings in the Application Model, implement the [ListEditor.SaveModel](xref:DevExpress.ExpressApp.Editors.ListEditor.SaveModel) method. Otherwise, leave this method empty

This code snippet demonstrates the steps above.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp.Templates;
using DevExpress.ExpressApp.Utils;
using DevExpress.ExpressApp.Win.Controls;
using DevExpress.ExpressApp.Win.SystemModule;
using DevExpress.Utils.Menu;
using DevExpress.XtraBars;
// ...
[ListEditor(typeof(IPictureItem))]
public class WinCustomListEditor : ListEditor, IControlOrderProvider {
	private System.Windows.Forms.ListView control;
	private System.Windows.Forms.ImageList images;
	private Object controlDataSource;
	private void dataSource_ListChanged(object sender, ListChangedEventArgs e) {
		Refresh();
	}
	private void control_MouseDoubleClick(object sender, MouseEventArgs e) {
		if(e.Button == MouseButtons.Left) {
			OnProcessSelectedItem();
		}
	}
	private void control_KeyDown(object sender, System.Windows.Forms.KeyEventArgs e) {
		if(e.KeyCode == Keys.Enter) {
			OnProcessSelectedItem();
		}
	}
	private void control_ItemSelectionChanged(object sender, System.Windows.Forms.ListViewItemSelectionChangedEventArgs e) {
		OnSelectionChanged();
	}
	private void control_SelectedIndexChanged(object sender, EventArgs e) {
		OnSelectionChanged();
		OnFocusedObjectChanged();
	}
	private System.Windows.Forms.ListViewItem FindByTag(object tag) {
		IPictureItem itemToSearch = (IPictureItem)tag;
		if(control != null && itemToSearch != null) {
			foreach(System.Windows.Forms.ListViewItem item in control.Items) {
				if(((IPictureItem)item.Tag).ID == itemToSearch.ID)
					return item;
			}
		}
		return null;
	}
	protected override object CreateControlsCore() {
		control = new System.Windows.Forms.ListView();
		control.Sorting = SortOrder.Ascending;
		images = new System.Windows.Forms.ImageList();
		images.ImageSize = new System.Drawing.Size(104, 150);
		images.ColorDepth = ColorDepth.Depth32Bit;
		control.LargeImageList = images;
		control.HideSelection = false;
		control.SelectedIndexChanged += control_SelectedIndexChanged;
		control.ItemSelectionChanged += control_ItemSelectionChanged;
		control.MouseDoubleClick += control_MouseDoubleClick;
		control.KeyDown += control_KeyDown;
		Refresh();
		return control;
	}
	protected override void AssignDataSourceToControl(Object dataSource) {
		if(dataSource is DevExpress.Xpo.XPServerCollectionSource) {
			throw new Exception("The WinCustomListEditor doesn't support Server mode and so cannot use an XPServerCollectionSource object as the data source.");
		}
		if(controlDataSource != dataSource) {
			IBindingList oldBindable = controlDataSource as IBindingList;
			if(oldBindable != null) {
				oldBindable.ListChanged -= new ListChangedEventHandler(dataSource_ListChanged);
			}
			controlDataSource = dataSource;
			IBindingList bindable = controlDataSource as IBindingList;
			if(bindable != null) {
				bindable.ListChanged += dataSource_ListChanged;
			}
			Refresh();
		}
	}
	public WinCustomListEditor(IModelListView info)
		: base(info) {
	}
	public override void Dispose() {
		controlDataSource = null;
		base.Dispose();
	}
	public override void Refresh() {
		if(control == null)
			return;
		object focused = FocusedObject;
		control.SelectedItems.Clear();
		try {
			control.BeginUpdate();
			images.Images.Clear();
			control.Items.Clear();
			if(ListHelper.GetList(controlDataSource) != null) {
				images.Images.Add(ImageLoader.Instance.GetImageInfo("NoImage").Image);
				foreach(IPictureItem item in ListHelper.GetList(controlDataSource)) {
					int imageIndex = 0;
					if(item.Image != null) {
						images.Images.Add(item.Image);
						imageIndex = images.Images.Count - 1;
					}
					System.Windows.Forms.ListViewItem lItem =
						new System.Windows.Forms.ListViewItem(item.Text, imageIndex);
					lItem.Tag = item;
					control.Items.Add(lItem);
				}
			}
		}
		finally {
			control.EndUpdate();
		}

		FocusedObject = focused;
		if(FocusedObject == null && control.Items.Count > 1) {
			FocusedObject = control.Items[0].Tag;
		}
	}
	public override IList GetSelectedObjects() {
		if(control == null)
			return new object[0] { };

		object[] result = new object[control.SelectedItems.Count];
		for(int i = 0; i < control.SelectedItems.Count; i++) {
			result[i] = control.SelectedItems[i].Tag;
		}
		return result;
	}
	public override void SaveModel() {
	}
	public override SelectionType SelectionType {
		get { return SelectionType.Full; }
	}
	public override object FocusedObject {
		get {
			return (control != null) && (control.FocusedItem != null) ? control.FocusedItem.Tag : null;
		}
		set {
			System.Windows.Forms.ListViewItem item = FindByTag(value);
			if(item != null) {
				control.SelectedItems.Clear();
				
				item.Focused = true;
				item.Selected = true;
			}
		}
	}
    #region IControlOrderProvider
    // Implementing these methods is essential for the proper functioning 
    // of the Previous Object and Next Object Actions in non-client modes.
    public int GetIndexByObject(object obj) {
        var items = ListHelper.GetList(controlDataSource);
        var index = items.IndexOf(obj);
        if(index == int.MinValue) {
            index = -1;
        }
        return index;
    }
    public object GetObjectByIndex(int index) {
        var items = ListHelper.GetList(controlDataSource);
        return items[index];
    }
    public IList GetOrderedObjects() {
        var orderedObjects = new List<object>();
        var items = ListHelper.GetList(controlDataSource);
        for(var rowVisibleIndex = 0; rowVisibleIndex < items.Count; ++rowVisibleIndex) {
            var record = items[rowVisibleIndex];
            if(record != null) {
                orderedObjects.Add(record);
            }
        }
        return orderedObjects;
    }
    #endregion
}
```
***
