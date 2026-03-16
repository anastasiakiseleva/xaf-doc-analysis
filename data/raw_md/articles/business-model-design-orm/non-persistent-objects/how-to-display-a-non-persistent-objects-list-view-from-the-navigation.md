---
uid: "114052"
seealso:
- linkId: "113471"
- linkId: "114516"
title: "How to: Display a Non-Persistent Object's List View from the Navigation"
owner: Ekaterina Kiseleva
---
# How to: Display a Non-Persistent Object's List View from the Navigation

This example demonstrates how to display a List View with [non-persistent objects](xref:116516) from the [Navigation](xref:113198). Note that this approach is compatible with [Client](xref:118449) data access mode only.

1. Declare a non-persistent class (for example, `MyNonPersistentObject`), and decorate it with the [DomainComponent](xref:DevExpress.ExpressApp.DC.DomainComponentAttribute) and [DefaultClassOptions](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) attributes.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.DC;
	using DevExpress.Persistent.Base;
	// ...
	[DomainComponent, DefaultClassOptions]
	public class MyNonPersistentObject {
	    // ...
	}
	```
	
	***
	
	> [!NOTE]
	> [!include[NonPersistent_RecommendedInterfaces](~/templates/nonpersistent_recommendedinterfaces111883.md)]
2. [!include[](~/templates/nonpersistentosproviderregistration111293.md)]
	
	At this step, you can run the application and see that the Navigation shows the **My Non Persistent Object** navigation item. It opens the empty List View and you can click the New Action to create non-persistent objects. However, all created objects are removed when you reopen the List View.

	![Empty List View](~/images/NonPersistentListViewInNavigation_empty.png)

3. To fill the List View in code, subscribe to the @DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated event in the Application Builder code. In the event handler, subscribe to the [NonPersistentObjectSpace.ObjectsGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting) event. In the `ObjectsGetting` handler, check if the requested object type is `MyNonPersistentObject` and populate the `e.Objects` collection with new objects.
	
    **File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp;
	using System.ComponentModel;
	// ...
	builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
		var nonPersistentObjectSpace = context.ObjectSpace as NonPersistentObjectSpace;
		if (nonPersistentObjectSpace != null) {
			nonPersistentObjectSpace.ObjectsGetting += NonPersistentObjectSpace_ObjectsGetting;
		}
	};
	// ...
    private void NonPersistentObjectSpace_ObjectsGetting(object sender, ObjectsGettingEventArgs e) {
        if (e.ObjectType == typeof(MyNonPersistentObject)) {
            BindingList<MyNonPersistentObject> objects = new BindingList<MyNonPersistentObject>();
            for (int i = 1; i < 10; i++) {
                objects.Add(new MyNonPersistentObject() { Name = string.Format("Object {0}", i) });
            }
            e.Objects = objects;
        }
    }
	```
	
	***
	
	> [!TIP]
	> You can also sort and filter List View contents when the List View's data source is shaped. To do this, use the `DynamicCollection` class instead of `BindingList`. Handle the `DynamicCollection.FetchObjects` event and pass a filtered collection to the `e.Objects` argument. This event is raised after a View's data source is reloaded or its sort/filter parameters are changed. Use the `Sorting`, `Criteria`, and other event arguments to shape the collection. The following example demonstrates how to implement this: [How to filter and sort Non-Persistent Objects](https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Filtering-Demo).
	
The image below demonstrates the result.

![NonPersistentListViewInNavigation](~/images/nonpersistentlistviewinnavigation118292.png)

> [!TIP]
> [!include[NonPersistentObjectSpace.ModifiedObjects Note](~/templates/nonpersistentobjectspace.modifiedobjects-note111302.md)]