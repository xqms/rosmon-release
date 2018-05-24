Name:           ros-kinetic-rosmon
Version:        1.0.4
Release:        0%{?dist}
Summary:        ROS rosmon package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ncurses-devel
Requires:       ros-kinetic-cmake-modules
Requires:       ros-kinetic-message-generation
Requires:       ros-kinetic-rosbash
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rospack
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-cpp
Requires:       ros-kinetic-std-msgs
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  ncurses-devel
BuildRequires:  python-devel
BuildRequires:  python-rospkg
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-kinetic-catch-ros
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-rosbash
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslib
BuildRequires:  ros-kinetic-rospack
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rqt-gui
BuildRequires:  ros-kinetic-rqt-gui-cpp
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  yaml-cpp-devel

%description
Node launcher and monitor for ROS. rosmon is a replacement for the roslaunch
tool, focused on performance, remote monitoring, and usability.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu May 24 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.4-0
- Autogenerated by Bloom

* Sat May 05 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.3-0
- Autogenerated by Bloom

* Tue Apr 24 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.2-0
- Autogenerated by Bloom

* Fri Apr 13 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.1-0
- Autogenerated by Bloom

* Fri Apr 13 2018 Max Schwarz <max.schwarz@uni-bonn.de> - 1.0.0-0
- Autogenerated by Bloom

