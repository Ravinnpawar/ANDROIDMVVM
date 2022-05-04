package br.com.ht7.androidmvvm.models;

import java.lang.System;

@kotlin.Metadata(mv = {1, 1, 16}, bv = {1, 0, 3}, k = 1, d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0002\bf\u0018\u00002\u00020\u0001J\u0014\u0010\u0002\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020\u00050\u00040\u0003H\'J\u0014\u0010\u0006\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020\u00050\u00040\u0003H\'\u00a8\u0006\u0007"}, d2 = {"Lbr/com/ht7/androidmvvm/models/CountryApi;", "", "all", "Lio/reactivex/Single;", "", "Lbr/com/ht7/androidmvvm/models/Country;", "some", "app_debug"})
public abstract interface CountryApi {
    
    @org.jetbrains.annotations.NotNull()
    @retrofit2.http.GET(value = "all")
    public abstract io.reactivex.Single<java.util.List<br.com.ht7.androidmvvm.models.Country>> all();
    
    @org.jetbrains.annotations.NotNull()
    @retrofit2.http.GET(value = "all")
    public abstract io.reactivex.Single<java.util.List<br.com.ht7.androidmvvm.models.Country>> some();
}