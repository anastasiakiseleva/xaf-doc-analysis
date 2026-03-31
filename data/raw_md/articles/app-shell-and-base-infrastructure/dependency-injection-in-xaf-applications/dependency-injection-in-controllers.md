---
uid: "404402"
title: Dependency Injection in Controllers
seealso:
  - linkId: "404430"
---
# Dependency Injection in Controllers

To obtain dependencies, the corresponding constructor of the Controller class must be decorated with the [ActivatorUtilitiesConstructorAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.activatorutilitiesconstructorattribute).

## Constructor Injection with IServiceProvider Parameter (Preferred Method)

If your application implements multiple Controllers that use dependency injection, we recommend that you use @System.IServiceProvider as shown in the following example. This technique works faster compared to the one where you pass individual services as parameters to the Controller class constructor.

```csharp{14,15}
public class DependencyInjectionServiceProviderSampleController : Controller { 

    private SimpleAction simpleAction; 
    private readonly IServiceProvider serviceProvider; 

    // Use a constructor without parameters to initialize Actions.
    // This is necessary for the correct work of the Model Editor.
    public DependencyInjectionServiceProviderSampleController() { 
        simpleAction = new SimpleAction(this, "SimpleAction", PredefinedCategory.RecordEdit); 
        simpleAction.Execute += SimpleAction_Execute; 
    } 

    // Implement this constructor to support dependency injection.
    [ActivatorUtilitiesConstructor] 
    public DependencyInjectionServiceProviderSampleController(IServiceProvider serviceProvider) : this() { 
        this.serviceProvider = serviceProvider; 
    } 

    private void DoWork() { 
      var serviceOne = serviceProvider.GetRequiredService<IServiceOne>(); 
      var serviceTwo = serviceProvider.GetRequiredService<IServiceTwo>(); 
      //...  
    } 

} 
```
> [!IMPORTANT]
> The constructor without parameters (`this()`) is required for Model Editor operation.
>
> By design, you cannot declare Actions or call the `InitializeComponent()` method in the constructor for dependency injection.

## Constructor Injection with Individual Services As Parameters

Alternatively, you can pass services as parameters to the Controller class constructor.

```csharp{20,21}
public interface IServiceOne { } 
public interface IServiceTwo { } 

public class ConcreteServiceOne : IServiceOne { } 
public class ConcreteServiceTwo : IServiceTwo { } 

public class DependencyInjectionSampleController : Controller { 
    private SimpleAction simpleAction; 
    private readonly IServiceOne serviceOne; 
    private readonly IServiceTwo serviceTwo; 

    // Use a constructor without parameters to initialize Actions.
    // This is necessary for the correct work of the Model Editor.
    public DependencyInjectionSampleController() { 
        simpleAction = new SimpleAction(this, "SimpleAction", PredefinedCategory.RecordEdit); 
        simpleAction.Execute += SimpleAction_Execute; 
    } 

    // Implement this constructor to support dependency injection.
    [ActivatorUtilitiesConstructor] 
    public DependencyInjectionSampleController(IServiceOne serviceOne, IServiceTwo serviceTwo) : this() { 
        this.serviceOne = serviceOne; 
        this.serviceTwo = serviceTwo; 
    } 
 
} 
```
