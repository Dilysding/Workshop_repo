# # Case 1
function traj(ds::DiscreteDynamicalSystem, t::Int, u = ds.u0; kwargs...)
    i = integrator(ds, u)
    trajdiscr(i, t; kwargs...)
end

function trajdiscr(i, t; dt::Int = 1, ttr::Int = 0)
    t0 = current_time(i)
    timevec = (t0+ttr):dt:(t0+total_time+ttr)
    ttr ≠ 0 && step!(i, ttr)
    state = Vector{typeof((get_state(i))}(undef, L)
    state = [get_state(i)]
    for i in 2:length(timevec)
        step!(i, dt)
        push!(state, get_state(i))
    end
    return timevec, state
end

# Case 2
function sat_pres(t)
    e_water_t = e_eq_water_mk.(t)
    e_ice_t = e_eq_ice_mk.(t)
    water = t .> constants.Ttr
    ice = t .< (constants.Ttr - 23.0)

    e = @. (
        e_ice_t
        + (e_water_t - e_ice_t)
        * ((t - constants.Ttr + 23) / 23) ^ 2
    )
    e[ice] = e_ice_t[water]
    e[water] = e_water_t[water]
    return e
end