# IoC (Inversion of Control)

- 传统的应用程序中，控制权在程序本身（紧密耦合）。如果要使用一个组件，必须先知道如何正确地创建和配置它。
- 在IoC模式下，控制权发生了反转，即从应用程序转移到了IoC容器，所有组件不再由应用程序自己创建和配置，而是由IoC容器负责，这样，应用程序只需要直接使用已经创建好并且配置好的组件。

## DI (Dependency Injection）

- DI解决了一个最主要的问题：将组件的创建+配置与组件的使用相分离，由IoC容器负责管理组件的生命周期。
  - 属性注入
    - 最简单的配置是通过XML文件来实现
    - 通过`set()`方法实现
  - 构造方法注入

## 无侵入容器

- 在设计上，Spring的IoC容器是一个高度可扩展的无侵入容器。
- 所谓无侵入，是指应用程序的组件无需实现Spring的特定接口，或者说，组件根本不知道自己在Spring的容器中运行。

## JavaBean

在Spring的IoC容器中，我们把所有组件统称为JavaBean，即配置一个组件就是配置一个Bean。

IoC容器如何创建组件，以及各组件的依赖关系。一种最简单的配置是通过XML文件来实现。

```xml
<beans>
    <bean id="dataSource" class="HikariDataSource" />
    <bean id="bookService" class="BookService">
        <property name="dataSource" ref="dataSource" />
    </bean>
    <bean id="userService" class="UserService">
        <property name="dataSource" ref="dataSource" />
    </bean>
</beans>
```

## 接口BeanFactory和ApplicationContext的区别

- BeanFactory的实现是按需创建，即第一次获取Bean时才创建这个Bean。
- ApplicationContext会一次性创建所有的Bean。
  - 实际上，ApplicationContext接口是从BeanFactory接口继承而来的，并且，ApplicationContext提供了一些额外的功能，包括国际化支持、事件和通知机制等。通常情况下，我们总是使用ApplicationContext，很少会考虑使用BeanFactory。

## 总结

使用Spring的IoC容器，实际上就是通过类似XML这样的配置文件，把我们自己的Bean的依赖关系描述出来，然后让容器来创建并装配Bean。一旦容器初始化完毕，我们就直接从容器中获取Bean使用它们。

使用XML配置的优点是所有的Bean都能一目了然地列出来，并通过配置注入能直观地看到每个Bean的依赖。它的缺点是写起来非常繁琐，每增加一个组件，就必须把新的Bean配置到XML中。