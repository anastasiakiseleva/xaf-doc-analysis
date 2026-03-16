---
uid: "113471"
seealso:
- linkId: "113259"
- linkId: "113167"
- linkId: "114052"
title: "How to: Display a Non-Persistent Object's Detail View"
owner: Ekaterina Kiseleva
---
# How to: Display a Non-Persistent Object's Detail View

## Show a Non-Persistent Object from the Navigation

1. Declare a non-persistent class, apply the [](xref:DevExpress.ExpressApp.DC.DomainComponentAttribute) to it, and add an [object key property](xref:DevExpress.ExpressApp.Data.KeyAttribute).
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using System.ComponentModel;
	using DevExpress.ExpressApp.DC;
	// ...
	[DomainComponent]
	public class NonPersistentObject {
	    [Browsable(false)]
	    [DevExpress.ExpressApp.Data.Key]
	    public int Oid { get; set; }
	    public string Name { get; set; }
	}
	```

	***
	
	> [!NOTE]
	> [!include[NonPersistent_RecommendedInterfaces](~/templates/nonpersistent_recommendedinterfaces111883.md)]
2.  Rebuild the solution.
3.  [Run the Model Editor](xref:113326) for a module project and [add a new navigation item](xref:402131). Set the [IModelNavigationItem.View](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.View) property to the identifier of the Detail View to be displayed (for example, **NonPersistentObject_DetailView**). Set the [IModelNavigationItem.ObjectKey](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.ObjectKey) property to an arbitrary integer value. Note that this value should be unique if you want to display different non-persistent objects of this type.
	
	![NonPersistentKey](~/images/nonpersistentkey123148.png)
	
4. [!include[NonPersistentOSProviderRegistration](~/templates/nonpersistentosproviderregistration111293.md)]
5. In the Application Builder code, subscribe to the @DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated event. In the event handler, subscribe to the [NonPersistentObjectSpace.ObjectByKeyGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectByKeyGetting) event. In the `ObjectByKeyGetting` event handler, check if the requested object type is `NonPersistentObject`. If so, pass a `NonPersistentObject` instance with the key value specified in step _3_ as the `e.Object` event parameter.

    **File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

	# [C#](#tab/tabid-csharp)
	
	```csharp
	using System;
	using DevExpress.ExpressApp;
	// ...
	builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
		var nonPersistentObjectSpace = context.ObjectSpace as NonPersistentObjectSpace;
		if (nonPersistentObjectSpace != null) {
			nonPersistentObjectSpace.ObjectByKeyGetting += nonPersistentObjectSpace_ObjectByKeyGetting;
		}
	};
	// ...
    private void nonPersistentObjectSpace_ObjectByKeyGetting(object sender, ObjectByKeyGettingEventArgs e) {
        IObjectSpace objectSpace = (IObjectSpace)sender;
        if (e.ObjectType.IsAssignableFrom(typeof(NonPersistentObject))) {
            if (((int)e.Key) == 138) {
                NonPersistentObject obj138 = objectSpace.CreateObject<NonPersistentObject>();
                obj138.Oid = 138;
                obj138.Name = "Sample Object";
                e.Object = obj138;
            }
        }
    }
	```

	***

	To create a new non-persistent object for each Detail View, leave the `ObjectKey` value empty in the Model Editor and create the following View Controller instead of the code above:

	# [C#](#tab/tabid-csharp)

	```csharp
	using DevExpress.ExpressApp;
	// ...
	public class NonPersistentObjectActivatorController : ObjectViewController<DetailView, NonPersistentObject> {
		protected override void OnActivated() {
			base.OnActivated();
			if ((ObjectSpace is NonPersistentObjectSpace) && (View.CurrentObject == null)) {
				View.CurrentObject = ObjectSpace.CreateObject(View.ObjectTypeInfo.Type);
				View.ViewEditMode = DevExpress.ExpressApp.Editors.ViewEditMode.Edit;
			}
		}
	}
	```

	***

	When you use the @DevExpress.ExpressApp.IObjectSpace.CreateObject(System.Type) method to create an object, the Object Space considers this object as new. In this case, the Save confirmation dialog is displayed when you close the object View. If you do not want to show this dialog, call the [NonPersistentObjectSpace.RemoveFromModifiedObjects](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.RemoveFromModifiedObjects(System.Object)) method that marks this object as existing and not changed. 

	The [NonPersistentObjectSpace.CreateObject](xref:DevExpress.ExpressApp.IObjectSpace.CreateObject(System.Type)) method uses the default constructor to create an object within the Object Space. If you want to use another constructor, create a new object and add it to the Object Space manually. For this purpose, pass this object to the [NonPersistentObjectSpace.GetObject](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.GetObject(System.Object)) method. This allows the Object Space to track changes made to the new object (if it implements the @System.ComponentModel.INotifyPropertyChanged interface and the @DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChange option is enabled).

## Show Non-Persistent Objects in a Dashboard View

To show non-persistent objects in a @DevExpress.ExpressApp.DashboardView, follow the steps from the previous section and [create a dashboard item](xref:113296) instead of the navigation item. Refer to the @DevExpress.ExpressApp.DashboardView class description for information on how a Detail View binds to a Dashboard View item. 

## Show a Non-Persistent Object in a Modal Dialog Window

1. Implement a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) Action. 
2. Handle its [PopupWindowShowAction.CustomizePopupWindowParams](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams) event. 
3. In the event handler: 

	* Use the @DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type) method to create an Object Space for the non-persistent type.
    * Use the [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,System.Object)) method to create a Detail View for the non-persistent type.
	* Set the [CustomizePopupWindowParamsEventArgs.View](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.View) property to this Detail View.

Refer to the following topics for more information and examples:
- [Ways to Show a View](xref:112803)
- [Ways to Show a Confirmation Dialog](xref:118240)

## Show a Non-Persistent Dialog from a Business Class

To execute simple business logic and prompt a user for parameters, use the [](xref:DevExpress.Persistent.Base.ActionAttribute) as shown in the [How to: Create an Action Using the Action Attribute](xref:112619#create-an-action-that-displays-a-pop-up-dialog) topic.
