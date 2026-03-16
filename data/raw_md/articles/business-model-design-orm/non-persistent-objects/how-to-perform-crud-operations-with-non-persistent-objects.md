---
uid: "115672"
title: 'How to: Perform CRUD Operations with Non-Persistent Objects'
seealso:
- linkId: "117395"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF-CRUD-for-Non-Persistent-Objects-Stored-Remotely
  altText: 'GitHub Example: XAF - How to Implement CRUD Operations for Non-Persistent Objects Stored Remotely'
---
# How to: Perform CRUD Operations with Non-Persistent Objects

Follow the steps below to implement the _Create_, _Read_, _Update_, and _Delete_ operations for [non-persistent objects](xref:116516).

1. Implement the following non-persistent class:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
    using DevExpress.ExpressApp.DC;
    using DevExpress.ExpressApp;
    using DevExpress.Persistent.Base;
    // ...
    [DomainComponent]
    public class CustomNonPersistentObject : NonPersistentObjectCloneable {
        private string name;

        public CustomNonPersistentObject() : base() { }
        public CustomNonPersistentObject(Guid oid) : base(oid) { }

        public string Name {
            get { return name; }
            set {
                if (name != value) {
                    name = value;
                    OnPropertyChanged(nameof(Name));
                }
            }
        }

        public override NonPersistentObjectCloneable Clone(IObjectMap map) {
            var result = (CustomNonPersistentObject)base.Clone(map);
            result.name = name;
            return result;
        }
    }

    public abstract class NonPersistentObjectCloneable : NonPersistentBaseObject {
        public NonPersistentObjectCloneable() : base() { }
        public NonPersistentObjectCloneable(Guid oid) : base(oid) { }
        public virtual NonPersistentObjectCloneable Clone(IObjectMap map) {
            var clone = (NonPersistentObjectCloneable)Activator.CreateInstance(this.GetType(), Oid);
            map.AcceptObject(clone);
            return clone;
        }
    }
	```

	***

    Note that the non-persistent class in the example above inherits the base `NonPersistentBaseObject`. The logic implemented in the base class is required so that a non-persistent object's copies can be created and distributed between underlying storages. For information on why this is required, see the following section: [Non-Persistent Object Spaces Cannot Share Objects that Implement IObjectSpaceLink](#2-non-persistent-object-spaces-cannot-share-objects-that-implement-iobjectspacelink).
    
    The `IObjectMap` interface defines an abstract dictionary of all created non-persistent objects. This interface will be introduced later in this tutorial.

2. Open the application's `Startup.cs` file and ensure that the `NonPersistentObjectSpaceProvider` is registered. The [Template Kit](xref:405447) adds this code automatically. Note that this code may be missing if you created your project in an older XAF version:

    **File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp
    // ...
    builder.ObjectSpaceProviders
        // ...
        .AddNonPersistent();
    // ...
    ```

    ***

3. Next, implement a global storage for non-persistent objects. The storage must implement all required CRUD operations:

	# [C#](#tab/tabid-csharp)
	
	```csharp
    using System.Collections.Concurrent;
    // ...
    // The `IObjectMap` interface defines an abstract dictionary of all created non-persistent objects.
    public interface IObjectMap {
        object GetObject(object obj);
        void AcceptObject(object obj);
    }

    public class NonPersistentGlobalObjectStorage : IObjectMap {
        public ConcurrentDictionary<Guid, NonPersistentObjectCloneable> objectsCache { get; } = new();
        public IEnumerable<NonPersistentObjectCloneable> Objects { get { return objectsCache.Values; } }

        public NonPersistentGlobalObjectStorage() {
            CreateObject<CustomNonPersistentObject>("A");
            CreateObject<CustomNonPersistentObject>("B");
            CreateObject<CustomNonPersistentObject>("C");
        }
        private NonPersistentObjectCloneable CreateObject<T>(string value) where T : NonPersistentObjectCloneable, new() {
            T result = new T();
            if (result is CustomNonPersistentObject custom) {
                custom.Name = value;
            }
            objectsCache.TryAdd(result.Oid, result);
            return result;
        }

        public void Add(NonPersistentObjectCloneable obj) {
            objectsCache.TryAdd(obj.Oid, obj);
        }
        public NonPersistentObjectCloneable FindObject(Guid key) {
            NonPersistentObjectCloneable result;
            objectsCache.TryGetValue(key, out result);
            return result;
        }
        public void SaveObject(NonPersistentObjectCloneable obj) {
            var found = FindObject(obj.Oid);
            var clone = obj.Clone(this);
            if (found != null) {
                NonPersistentObjectCloneable value;
                objectsCache.TryRemove(found.Oid, out value);
            }
            objectsCache.TryAdd(clone.Oid, clone);
        }
        public void DeleteObject(NonPersistentObjectCloneable obj) {
            var found = FindObject(obj.Oid);
            if (found != null) {
                NonPersistentObjectCloneable value;
                objectsCache.TryRemove(found.Oid, out value);
            }
        }
        object IObjectMap.GetObject(object obj) {
            var keyObj = obj as NonPersistentObjectCloneable;
            if (keyObj != null) {
                return FindObject(keyObj.Oid) ?? throw new KeyNotFoundException(keyObj.Oid.ToString());
            }
            else {
                return obj;
            }
        }
        void IObjectMap.AcceptObject(object obj) {
        }
    }
	```

	***

4. Register your custom storage as a singleton service in the application's `Startup.cs` file:

    **File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp
    // ...
    services.AddSingleton<NonPersistentGlobalObjectStorage>();
    // ...
    ```

    ***

    > [!NOTE]
    > In this step and in _step 6_, it may be beneficial to move all configuration logic to the main module (_MySolution.Module_) as described in the following help topic: [](xref:405025). This way, you do not need to repeat the same lines across all _Startup.cs_ files of the platform-specific application projects.

5. Extend the application's Non-Persistent Object Spaces so that they use your custom storage to store objects. To do this, you can implement a `NonPersistentObjectSpaceExtender` class that encapsulates the logic that accesses all required services and handles all required events for every created `NonPersistentObjectSpace`:

	# [C#](#tab/tabid-csharp)
	
	```csharp
    using DevExpress.ExpressApp.Core;
    using DevExpress.ExpressApp;
    using Microsoft.Extensions.DependencyInjection;
    using System.ComponentModel
    // ...
    public class NonPersistentObjectSpaceExtender : IObjectMap {
        readonly NonPersistentObjectSpace objectSpace;
        readonly NonPersistentGlobalObjectStorage globalObjects;
        readonly Dictionary<Guid, NonPersistentObjectCloneable> localObjects;

        public NonPersistentObjectSpaceExtender(IServiceProvider serviceProvider, NonPersistentObjectSpace nonPersistentObjectSpace) {
            objectSpace = nonPersistentObjectSpace;
            globalObjects = serviceProvider.GetRequiredService<NonPersistentGlobalObjectStorage>();
            localObjects = new Dictionary<Guid, NonPersistentObjectCloneable>();

            objectSpace.Committing += ObjectSpace_Committing;
            objectSpace.ObjectsGetting += ObjectSpace_ObjectsGetting;
            objectSpace.ObjectByKeyGetting += ObjectSpace_ObjectByKeyGetting;
            objectSpace.ObjectGetting += ObjectSpace_ObjectGetting;
            objectSpace.Reloaded += ObjectSpace_Reloaded;
            objectSpace.Disposed += ObjectSpace_Disposed;
            objectSpace.ModifiedChanging += NonPersistentObjectSpace_ModifiedChanging;

            var objectSpaceProviderService = serviceProvider.GetRequiredService<IObjectSpaceProviderService>();
            var objectSpaceCustomizerService = serviceProvider.GetRequiredService<IObjectSpaceCustomizerService>();
            objectSpace.PopulateAdditionalObjectSpaces(objectSpaceProviderService, objectSpaceCustomizerService);
        }

        object IObjectMap.GetObject(object obj) {
            return objectSpace.GetObject(obj);
        }
        void IObjectMap.AcceptObject(object obj) {
            var keyObj = obj as NonPersistentObjectCloneable;
            if (keyObj != null) {
                localObjects.Add(keyObj.Oid, keyObj);
            }
        }
        private NonPersistentObjectCloneable GetObject(NonPersistentObjectCloneable obj) {
            if (!objectSpace.IsNewObject(obj)) {
                return GetObjectByKey(obj.Oid);
            }
            else {
                return obj;
            }
        }
        private NonPersistentObjectCloneable GetObjectByKey(Guid key) {
            NonPersistentObjectCloneable obj;
            if (!localObjects.TryGetValue(key, out obj)) {
                obj = LoadObject(key);
            }
            return obj;
        }
        private NonPersistentObjectCloneable LoadObject(Guid key) {
            var obj = globalObjects.FindObject(key);
            if (obj != null) {
                var clone = obj.Clone(this);
                ((IObjectSpaceLink)clone).ObjectSpace = objectSpace;
                return clone;
            }
            return null;
        }
        private void ObjectSpace_ObjectsGetting(Object sender, ObjectsGettingEventArgs e) {
            if (typeof(NonPersistentObjectCloneable).IsAssignableFrom(e.ObjectType)) {
                var objects = new BindingList<NonPersistentObjectCloneable>();
                objects.AllowNew = true;
                objects.AllowEdit = true;
                objects.AllowRemove = true;
                foreach (NonPersistentObjectCloneable obj in globalObjects.Objects) {
                    if (e.ObjectType.IsAssignableFrom(obj.GetType())) {
                        objects.Add(GetObject(obj));
                    }
                }
                e.Objects = objects;
            }
        }
        private void ObjectSpace_ObjectByKeyGetting(Object sender, ObjectByKeyGettingEventArgs e) {
            if (typeof(NonPersistentObjectCloneable).IsAssignableFrom(e.ObjectType) && e.Key is Guid) {
                e.Object = GetObjectByKey((Guid)e.Key);
            }
        }
        private void ObjectSpace_ObjectGetting(object sender, ObjectGettingEventArgs e) {
            var obj = e.SourceObject as NonPersistentObjectCloneable;
            if (obj != null) {
                e.TargetObject = GetObject(obj);
            }
        }
        private void ObjectSpace_Committing(Object sender, CancelEventArgs e) {
            var objectSpace = (NonPersistentObjectSpace)sender;
            foreach (Object obj in objectSpace.ModifiedObjects) {
                NonPersistentObjectCloneable baseObj = obj as NonPersistentObjectCloneable;
                if (baseObj != null) {
                    if (objectSpace.IsDeletedObject(baseObj)) {
                        globalObjects.DeleteObject(baseObj);
                    }
                    else {
                        globalObjects.SaveObject(baseObj);
                    }
                }
            }
        }
        private void ObjectSpace_Reloaded(object sender, EventArgs e) {
            localObjects.Clear();
        }
        private void NonPersistentObjectSpace_ModifiedChanging(object sender, ObjectSpaceModificationEventArgs e) {
            if (e.Object is NonPersistentObjectCloneable) {
                e.Cancel = false;
            }
        }
        private void ObjectSpace_Disposed(object sender, EventArgs e) {
            var objectSpace = (NonPersistentObjectSpace)sender;
            objectSpace.ObjectsGetting -= ObjectSpace_ObjectsGetting;
            objectSpace.ObjectByKeyGetting -= ObjectSpace_ObjectByKeyGetting;
            objectSpace.ObjectGetting -= ObjectSpace_ObjectGetting;
            objectSpace.Committing -= ObjectSpace_Committing;
            objectSpace.Reloaded -= ObjectSpace_Reloaded;
            objectSpace.ModifiedChanging -= NonPersistentObjectSpace_ModifiedChanging;
            objectSpace.Disposed -= ObjectSpace_Disposed;
        }
    }
	```

	***

    Note that this implementation of `NonPersistentObjectSpaceExtender` operates on its own local dictionary of non-persistent objects. The objects are cloned from/into the global storage when required so that each `NonPersistentObjectSpace` always has its own copies of the objects. For information on why this is required, see the following section: [Non-Persistent Object Spaces Cannot Share Objects that Implement IObjectSpaceLink](#2-non-persistent-object-spaces-cannot-share-objects-that-implement-iobjectspacelink).

6. To apply the `NonPersistentObjectSpaceExtender` to every created `NonPersistentObjectSpace`, add application builder code that handles the @DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated event as shown in the following code snippet:

    **File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp;
    // ...
    builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated += context => {
        if (context.ObjectSpace is NonPersistentObjectSpace nonPersistentObjectSpace) {
            new NonPersistentObjectSpaceExtender(context.ServiceProvider, nonPersistentObjectSpace);
        }
    };
    // ...
    ```

    ***

The following image demonstrates the result:

![Result](~/images/non-persistent-crud.png)

## Important Notes

### 1. Non-Persistent Object Spaces Do Not Track Changes

A non-persistent Object Space does not track changes of original objects and does not add changed objects to the @DevExpress.ExpressApp.IObjectSpace.ModifiedObjects collection. You can use the [IObjectSpace.SetModified(Object)](xref:DevExpress.ExpressApp.IObjectSpace.SetModified*) method to add changed objects to this collection explicitly. If a non-persistent object implements the [INotifyPropertyChanged](xref:System.ComponentModel.INotifyPropertyChanged) interface, you can set @DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChange / @DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChangeByDefault to **true** to automatically add the changed object to the @DevExpress.ExpressApp.IObjectSpace.ModifiedObjects collection when the @System.ComponentModel.INotifyPropertyChanged.PropertyChanged event is raised.

### 2. Non-Persistent Object Spaces Cannot Share Objects that Implement IObjectSpaceLink

[!include[DoNotShareNonPersistentObjects-note](~/templates/DoNotShareNonPersistentObjects-note.md)]
